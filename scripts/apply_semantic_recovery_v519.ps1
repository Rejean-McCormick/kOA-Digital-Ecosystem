param([switch]$Apply)
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7 -or !$Apply) { throw 'PowerShell 7 and -Apply required.' }
$manager = 'C:\mycode\Kristal\Kristal-Manager'
$private = Join-Path $env:LOCALAPPDATA 'Kristal'
New-Item -ItemType Directory -Path $private -Force | Out-Null
Push-Location -LiteralPath $manager
try {
    & python -m kristal_manager.semantic_recovery_v519 --locals 'C:\mycode\Kristal\locals' --public 'C:\mycode\Kristal\kristal-public' --private-dir $private --apply
    if ($LASTEXITCODE -ne 0) { throw 'V5.19 blocked; public unchanged.' }
} finally { Pop-Location }
