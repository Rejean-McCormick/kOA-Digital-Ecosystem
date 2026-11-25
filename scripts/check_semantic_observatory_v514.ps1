# Candidate private local semantic observatory: source trees are never edited.
param(
    [string]$Locals = 'C:\mycode\Kristal\locals',
    [string]$Manager = 'C:\mycode\Kristal\Kristal-Manager',
    [string]$OutputDirectory = (Join-Path $env:LOCALAPPDATA 'Kristal'),
    [string]$Python = 'python'
)
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) {
    throw 'PowerShell 7+ required.'
}
foreach ($root in @($Locals,$Manager)) {
    if (!(Test-Path -LiteralPath $root -PathType Container)) {
        throw "Missing required source directory: $root"
    }
}
if (!(Test-Path -LiteralPath (Join-Path $Manager 'kristal_manager\semantic_federation_inventory.py') -PathType Leaf)) {
    throw 'V5.14 Manager implementation is not installed at its exact root.'
}
if (!(Test-Path -LiteralPath $OutputDirectory -PathType Container)) {
    New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
}
$suffix = (Get-Date -Format 'yyyyMMdd_HHmmss') + '_' + [guid]::NewGuid().ToString('N').Substring(0,8)
$db = Join-Path $OutputDirectory "SEMANTIC_V514_$suffix.sqlite"
$report = Join-Path $OutputDirectory "SEMANTIC_V514_$suffix.json"
$old = $env:PYTHONPATH
try {
    $env:PYTHONPATH = $Manager
    & $Python -m kristal_manager build-semantic-observatory `
        --locals $Locals --db $db --report $report
    if ($LASTEXITCODE -ne 0) {
        throw "Semantic observatory blocked (exit $LASTEXITCODE). See $report. Source trees were not modified."
    }
    Write-Host 'SEMANTIC V5.14: CANDIDATE INTEGRITY PASS (not qualified)' -ForegroundColor Green
    Write-Host "Private SQLite: $db"
    Write-Host "Private report: $report"
}
finally {
    $env:PYTHONPATH = $old
}
