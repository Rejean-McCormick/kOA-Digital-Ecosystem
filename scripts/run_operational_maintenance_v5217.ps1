param([string]$Base='C:\mycode',[string]$Index='D:\EncyKlopedia\30_working\wikidata\wikidata.compact.sqlite',[string]$Dump='',[string]$RunId='')
$ErrorActionPreference='Stop'
if ($PSVersionTable.PSVersion.Major -lt 7 -or !$env:LOCALAPPDATA) { throw 'PowerShell 7 and LOCALAPPDATA required' }
$private=Join-Path $env:LOCALAPPDATA 'Kristal'
$k=Join-Path $Base 'Kristal'
if (!$RunId) { $RunId=if ($Dump) {'REPAIR_V5217_DUMP'} else {'REPAIR_V5217_COMPACT'} }
if ($RunId -notmatch '^[A-Za-z0-9_-]{1,64}$') { throw 'Invalid RunId' }
$output=Join-Path $private "maintenance\$RunId"
if (Test-Path -LiteralPath (Join-Path $output 'COMPLETE')) { throw 'Completed run is immutable; choose another RunId.' }
$argList=@('-m','kristal_manager.maintenance_repair_v5217','--locals',(Join-Path $k 'locals'),'--baseline',(Join-Path $private 'SEMANTIC_V52161_0cd971be254e1c9c'),'--scan',(Join-Path $private 'maintenance\RUN_20261126_234529_3215bda5'),'--output',$output,'--kristalizer',(Join-Path $k 'Kristalizer'),'--diag',(Join-Path $k 'KristalDiag'),'--index',$Index)
if ($Dump) { $argList+=@('--dump',$Dump) }
$env:PYTHONDONTWRITEBYTECODE='1'
Push-Location (Join-Path $k 'Kristal-Manager')
try { & python @argList; if ($LASTEXITCODE -ne 0) { throw 'Repair interrupted; re-run with same inputs.' } }
finally { Pop-Location }
