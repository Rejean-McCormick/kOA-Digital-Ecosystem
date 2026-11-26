# One local-first run: V5.17 canonical precedence, V5.16 active view, V5.18 total index.
param([switch]$Apply)
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 is required.' }
if (!$Apply) { throw 'Use -Apply to execute the one-shot local operation.' }

$kit = 'C:\mycode\Kristal\Kristal-Authoring-Kit'
$manager = 'C:\mycode\Kristal\Kristal-Manager'
$locals = 'C:\mycode\Kristal\locals'
$public = 'C:\mycode\Kristal\kristal-public'
$private = Join-Path $env:LOCALAPPDATA 'Kristal'
foreach ($root in @($kit, $manager, $locals, $public)) {
    if (!(Test-Path -LiteralPath $root -PathType Container)) {
        throw "Required local root missing: $root"
    }
}

New-Item -ItemType Directory -Path $private -Force | Out-Null
$kitScript = Join-Path $kit 'tools\v517_accepted_precedence.py'
if (!(Test-Path -LiteralPath $kitScript -PathType Leaf)) {
    throw 'V5.17 Authoring Kit operation is missing.'
}

& python $kitScript --locals $locals --private-dir $private --apply
if ($LASTEXITCODE -ne 0) {
    throw 'V5.17 local canonical step blocked. Check the private Kit progress report; public unchanged.'
}

$previousPythonPath = $env:PYTHONPATH
try {
    $env:PYTHONPATH = $manager
    & python -m kristal_manager.active_semantic_federation_v518 `
        --locals $locals --private-dir $private --public $public --apply
    if ($LASTEXITCODE -ne 0) {
        throw 'V5.18 active federation blocked. Canonical V5.17 progress is preserved; rerun after correction.'
    }
} finally {
    $env:PYTHONPATH = $previousPythonPath
}

Write-Host 'V5.18 ONE-SHOT LOCAL SEMANTIC FEDERATION: COMPLETE' -ForegroundColor Green
Write-Host 'Only local canonical Kit revisions and derived/private outputs were changed.'
Write-Host 'No public write, Git push, publication, or RuntimeSet activation.'
