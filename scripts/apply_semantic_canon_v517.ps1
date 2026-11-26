# V5.17 one local-first operation: Kit canonical precedence, then V5.16 read views.
param([switch]$Apply)
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 required.' }
$kit = 'C:\mycode\Kristal\Kristal-Authoring-Kit'
$manager = 'C:\mycode\Kristal\Kristal-Manager'
$locals = 'C:\mycode\Kristal\locals'
$private = Join-Path $env:LOCALAPPDATA 'Kristal'
foreach ($p in @($kit,$manager,$locals)) {
    if (!(Test-Path -LiteralPath $p -PathType Container)) { throw "Required local root missing: $p" }
}
New-Item -ItemType Directory -Path $private -Force | Out-Null
$script = Join-Path $kit 'tools\v517_accepted_precedence.py'
$pythonArgs = @($script, '--locals', $locals, '--private-dir', $private)
if ($Apply) { $pythonArgs += '--apply' }
& python @pythonArgs
if ($LASTEXITCODE -ne 0) { throw 'Canonical V5.17 evolution blocked; see private progress report. Public unchanged.' }
if ($Apply) {
    $oldPythonPath = $env:PYTHONPATH
    try {
        $env:PYTHONPATH = $manager
        & python -m kristal_manager.local_semantic_evolution_v516 `
            --locals $locals --private-dir $private --apply
        if ($LASTEXITCODE -ne 0) {
            throw 'Canonical revisions were selected, but V5.16 derived refresh failed. Rerun after resolving the blocker.'
        }
    } finally {
        $env:PYTHONPATH = $oldPythonPath
    }
    Write-Host 'V5.17 LOCAL CANONICAL EVOLUTION + V5.16 REFRESH: APPLIED' -ForegroundColor Green
} else {
    Write-Host 'V5.17 dry run complete. Nothing modified.' -ForegroundColor Yellow
}
