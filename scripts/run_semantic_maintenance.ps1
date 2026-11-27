param(
    [string]$Base = 'C:\mycode',
    [string]$Baseline = "$env:LOCALAPPDATA\Kristal\SEMANTIC_V52161_0cd971be254e1c9c",
    [string]$Index = 'D:\EncyKlopedia\30_working\wikidata\wikidata.compact.sqlite',
    [string]$Output = ''
)
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 required' }
if (!$Output) { $Output = Join-Path $env:LOCALAPPDATA ('Kristal\maintenance\RUN_' + (Get-Date -Format 'yyyyMMdd_HHmmss') + '_' + [guid]::NewGuid().ToString('N').Substring(0,8)) }
$k = Join-Path $Base 'Kristal'
Push-Location (Join-Path $k 'Kristal-Manager')
try {
    & python -m kristal_manager.maintenance_scan --locals (Join-Path $k 'locals') --baseline $Baseline --output $Output --kristalizer (Join-Path $k 'Kristalizer') --diag (Join-Path $k 'KristalDiag') --index $Index
    if ($LASTEXITCODE -ne 0) { throw 'Maintenance scan interrupted' }
    Write-Host "PRIVATE MAINTENANCE OUTPUT: $Output"
} finally { Pop-Location }
