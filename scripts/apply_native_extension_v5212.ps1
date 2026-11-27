$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 required' }
$manager = 'C:\mycode\Kristal\Kristal-Manager'
Push-Location $manager
try {
    & python -m kristal_manager.native_extension_v5212 --locals 'C:\mycode\Kristal\locals' --private-dir (Join-Path $env:LOCALAPPDATA 'Kristal') --kit 'C:\mycode\Kristal\Kristal-Authoring-Kit' --framework 'C:\mycode\Kristal\Kristal-Framework' --apply
    if ($LASTEXITCODE -ne 0) { throw 'V5.21.2 interrupted' }
} finally { Pop-Location }
