param([switch]$Apply,[switch]$Offline)
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7 -or !$Apply) { throw 'PowerShell 7 and -Apply required.' }
$private = Join-Path $env:LOCALAPPDATA 'Kristal'
$manager = 'C:\mycode\Kristal\Kristal-Manager'
$argList = @('-m','kristal_manager.semantic_qualification_v520','--locals','C:\mycode\Kristal\locals','--public','C:\mycode\Kristal\kristal-public','--private-dir',$private,'--kit','C:\mycode\Kristal\Kristal-Authoring-Kit','--framework','C:\mycode\Kristal\Kristal-Framework','--apply')
if ($Offline) { $argList += '--offline' } else { $argList += '--resume-latest' }
Push-Location -LiteralPath $manager
try { & python @argList; if ($LASTEXITCODE -ne 0) { throw 'V5.20 blocked or partial: inspect private report and Kit journal.' } }
finally { Pop-Location }
