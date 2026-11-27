$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 required' }
Push-Location 'C:\mycode\Kristal\Kristal-Manager'
try {
    & python -m kristal_manager.unified_native_v5215 --private-dir (Join-Path $env:LOCALAPPDATA 'Kristal') --kit 'C:\mycode\Kristal\Kristal-Authoring-Kit' --framework 'C:\mycode\Kristal\Kristal-Framework' --apply
    if ($LASTEXITCODE -ne 0) { throw 'V5.21.5 interrupted' }
} finally { Pop-Location }
