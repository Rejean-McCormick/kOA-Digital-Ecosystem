# Private read-only semantic reconciliation. Never selects revisions or writes canon/public.
param(
    [Parameter(Mandatory=$true)][string]$SourceDb,
    [string]$Manager = 'C:\mycode\Kristal\Kristal-Manager',
    [string]$OutputDirectory = (Join-Path $env:LOCALAPPDATA 'Kristal'),
    [string]$Python = 'python'
)
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) {
    throw 'PowerShell 7+ required.'
}
if (!(Test-Path -LiteralPath $SourceDb -PathType Leaf)) {
    throw "V5.14 SQLite introuvable : $SourceDb"
}
if (!(Test-Path -LiteralPath (Join-Path $Manager 'kristal_manager\semantic_reconciliation_v515.py') -PathType Leaf)) {
    throw 'Le module Manager V5.15 n est pas installé à la racine attendue.'
}
if (!(Test-Path -LiteralPath $OutputDirectory -PathType Container)) {
    New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
}
$suffix = (Get-Date -Format 'yyyyMMdd_HHmmss') + '_' + [guid]::NewGuid().ToString('N').Substring(0,8)
$review = Join-Path $OutputDirectory "SEMANTIC_V515_$suffix.sqlite"
$report = Join-Path $OutputDirectory "SEMANTIC_V515_$suffix.json"
$old = $env:PYTHONPATH
try {
    $env:PYTHONPATH = $Manager
    & $Python -m kristal_manager reconcile-semantic-observatory `
        --source-db $SourceDb --review-db $review --report $report
    if ($LASTEXITCODE -ne 0) {
        throw "Reconciliation blocked (exit $LASTEXITCODE). No canonical/public files changed."
    }
    Write-Host 'V5.15 REVIEW CANDIDATE CREATED — no selection, no qualification' -ForegroundColor Green
    Write-Host "Private review SQLite: $review"
    Write-Host "Private report JSON: $report"
}
finally {
    $env:PYTHONPATH = $old
}
