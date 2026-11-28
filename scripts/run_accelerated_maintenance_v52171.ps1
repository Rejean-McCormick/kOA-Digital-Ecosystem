param([string]$Base='C:\mycode',[string]$Index='D:\EncyKlopedia\30_working\wikidata\wikidata.compact.sqlite',[string]$Fast='D:\EncyKlopedia\30_working\wikidata-fast',[string]$Dump='D:\EncyKlopedia\10_sources\wikidata\dumps\current\wikidata-20260922-all.json.bz2')
$ErrorActionPreference='Stop'
if ($PSVersionTable.PSVersion.Major -lt 7 -or !$env:LOCALAPPDATA) { throw 'PS7 and LOCALAPPDATA required' }
$private=Join-Path $env:LOCALAPPDATA 'Kristal'
$k=Join-Path $Base 'Kristal'
$m=Join-Path $private 'maintenance'
$out=Join-Path $m ('ACCELERATED_V52171_'+(Get-Date -Format yyyyMMdd_HHmmss)+'_'+[guid]::NewGuid().ToString('N').Substring(0,8))
$env:PYTHONDONTWRITEBYTECODE='1'
Push-Location (Join-Path $k 'Kristal-Manager')
try {
    & python -m kristal_manager.maintenance_accelerated_v52171 --base (Join-Path $private 'SEMANTIC_V52161_0cd971be254e1c9c') --scan (Join-Path $m 'RUN_20261126_234529_3215bda5') --compact (Join-Path $m 'REPAIR_V5217_COMPACT') --partial (Join-Path $m 'REPAIR_V5217_DUMP') --index $Index --fast $Fast --dump $Dump --out $out --kristalizer (Join-Path $k 'Kristalizer') --diag (Join-Path $k 'KristalDiag')
    if ($LASTEXITCODE -ne 0) { throw 'Accelerated maintenance interrupted; prior runs unchanged.' }
    $zip=Join-Path $env:USERPROFILE ('Downloads\DIK_V52171_'+(Split-Path $out -Leaf)+'.zip')
    $paths=@('accelerated.sqlite','report.json','diagnostic.json','COMPLETE' | ForEach-Object { Join-Path $out $_ })
    Compress-Archive -LiteralPath $paths -DestinationPath $zip -CompressionLevel Optimal
    Get-FileHash -LiteralPath $zip -Algorithm SHA256
    Write-Host "VALIDATION ZIP: $zip"
} finally { Pop-Location }
