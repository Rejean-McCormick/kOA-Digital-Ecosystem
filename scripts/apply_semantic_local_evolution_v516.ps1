# Run one local-first semantic evolution. Never touches kristal-public.
param([switch]$Apply)
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 required.' }
$manager = 'C:\mycode\Kristal\Kristal-Manager'
$locals = 'C:\mycode\Kristal\locals'
$private = Join-Path $env:LOCALAPPDATA 'Kristal'
if (!(Test-Path -LiteralPath $manager -PathType Container)) { throw "Manager missing: $manager" }
if (!(Test-Path -LiteralPath $locals -PathType Container)) { throw "Local Kristals missing: $locals" }
New-Item -ItemType Directory -Path $private -Force | Out-Null
$old = $env:PYTHONPATH
try {
    $env:PYTHONPATH = $manager
    $pythonArgs = @('-m', 'kristal_manager.local_semantic_evolution_v516',
              '--locals', $locals, '--private-dir', $private)
    if ($Apply) { $pythonArgs += '--apply' }
    & python @pythonArgs
    if ($LASTEXITCODE -ne 0) { throw "Local evolution blocked (exit $LASTEXITCODE); public unchanged." }
    if ($Apply) {
        Write-Host 'V5.16 LOCAL DERIVED EVOLUTION: APPLIED' -ForegroundColor Green
    } else {
        Write-Host 'V5.16 DRY RUN: no local pointer changed.' -ForegroundColor Yellow
    }
} finally {
    $env:PYTHONPATH = $old
}
