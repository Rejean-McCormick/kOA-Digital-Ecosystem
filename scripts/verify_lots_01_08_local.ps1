# Read-only owner target SHA-256 comparison against dated, user-reported overlay manifests.
[CmdletBinding()]
param([switch]$ListOnly)
$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$ledgerPath = Join-Path $repoRoot 'docs/audit/2026-11-24-lots-01-08-evidence.v1.json'
$ledger = Get-Content -LiteralPath $ledgerPath -Raw -Encoding UTF8 | ConvertFrom-Json
$results = [System.Collections.Generic.List[object]]::new()
foreach ($lot in $ledger.lots) {
    foreach ($target in $lot.target_files) {
        $path = Join-Path -Path $target.root -ChildPath ($target.path.Replace('/', [IO.Path]::DirectorySeparatorChar))
        if ($ListOnly) {
            $status = 'UNVERIFIED'
        } elseif (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            $status = 'MISSING'
        } else {
            $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
            if ($hash -ceq $target.expected_post_install_sha256) { $status='MATCH' }
            else { $status='DRIFT' }
        }
        $results.Add([pscustomobject]@{Lot=$lot.lot; Repo=$target.repository; Path=$target.path; Status=$status})
    }
}
$results | Format-Table -AutoSize
$matched=@($results | Where-Object Status -EQ 'MATCH').Count
$missing=@($results | Where-Object Status -EQ 'MISSING').Count
$drift=@($results | Where-Object Status -EQ 'DRIFT').Count
if ($ListOnly) {
    Write-Host "READ ONLY: listed $($results.Count) targets; no on-disk verification requested."
} else {
    Write-Host "READ ONLY: MATCH=$matched | MISSING=$missing | DRIFT=$drift | TOTAL=$($results.Count)"
    Write-Host 'No repair, Git action, publishing or diK access performed.'
    if ($missing -gt 0 -or $drift -gt 0) { exit 2 }
}
