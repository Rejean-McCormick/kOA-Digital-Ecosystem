param([string]$Base='C:\mycode',[string]$Root='D:\EncyKlopedia',[int]$BatchSize=250,[int]$Timeout=600)
$ErrorActionPreference='Stop'
if ($PSVersionTable.PSVersion.Major -lt 7 -or !$env:LOCALAPPDATA) { throw 'PS7 and LOCALAPPDATA required' }
$private=Join-Path $env:LOCALAPPDATA 'Kristal'
$k=Join-Path $Base 'Kristal'
$factory=Join-Path $Base 'EncyKlopedia\EncyKlopedia\ecosystem\Kristal_UNESCO_Factory'
$env:PYTHONDONTWRITEBYTECODE='1'
Push-Location (Join-Path $k 'Kristal-Manager')
try {
    & python -B -c 'import indexed_bzip2'
    if ($LASTEXITCODE -ne 0) { throw 'indexed_bzip2 absent; no scan launched.' }
    $out=$null
    & python -m kristal_manager.maintenance_indexed_v5218 --base (Join-Path $private 'SEMANTIC_V52161_0cd971be254e1c9c\active.sqlite') --scan (Join-Path $private 'maintenance\RUN_20261126_234529_3215bda5\maintenance.sqlite') --root $Root --factory $factory --private $private --kristalizer (Join-Path $k 'Kristalizer') --diag (Join-Path $k 'KristalDiag') --batch-size $BatchSize --timeout $Timeout | ForEach-Object { Write-Host $_; if ($_ -like 'OUTPUT_PATH=*') { $out=$_.Substring(12) } }
    if ($LASTEXITCODE -ne 0 -or !$out) { throw 'Indexed maintenance interrupted. Completed batches retained; rerun same command.' }
    $zip=Join-Path $env:USERPROFILE ('Downloads\DIK_V5218_'+(Split-Path $out -Leaf)+'.zip')
    $paths=@('indexed.sqlite','report.json','diagnostic.json','COMPLETE' | ForEach-Object { Join-Path $out $_ })
    Compress-Archive -LiteralPath $paths -DestinationPath $zip -CompressionLevel Optimal
    Get-FileHash -LiteralPath $zip -Algorithm SHA256
    Write-Host "VALIDATION ZIP: $zip"
} finally { Pop-Location }
