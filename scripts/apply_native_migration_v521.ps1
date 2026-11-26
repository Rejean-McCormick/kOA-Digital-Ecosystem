param([switch]$Apply)
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7 -or !$Apply) { throw 'PowerShell 7 and -Apply required.' }
$private = Join-Path $env:LOCALAPPDATA 'Kristal'
Push-Location -LiteralPath 'C:\mycode\Kristal\Kristal-Manager'
try {
    & python -m kristal_manager.native_migration_v521 --locals 'C:\mycode\Kristal\locals' --private-dir $private --kit 'C:\mycode\Kristal\Kristal-Authoring-Kit' --framework 'C:\mycode\Kristal\Kristal-Framework' --apply
    if ($LASTEXITCODE -ne 0) { throw 'V5.21 blocked; inspect preceding error.' }
} finally { Pop-Location }
