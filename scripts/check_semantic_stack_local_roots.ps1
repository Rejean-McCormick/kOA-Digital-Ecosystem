<#
Read-only local verification of 14 reported worktree roots.
The manifest itself does not prove a checkout's origin or HEAD.
#>
param(
    [string]$RepoRoot = (Split-Path -Parent $PSScriptRoot),
    [switch]$RequireAll
)

$ErrorActionPreference = 'Stop'
$manifestPath = Join-Path $RepoRoot 'docs/inventory/semantic-stack-local-roots.v1.json'
$manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($manifest.schema -ne 'koa.semantic_stack.local_roots.v1') {
    throw 'Unexpected semantic-stack local root schema.'
}

$gitCommand = Get-Command git -ErrorAction SilentlyContinue
$results = @(
    foreach ($entry in $manifest.entries) {
        $checkout = [string]$entry.local_root
        $exists = Test-Path -LiteralPath $checkout -PathType Container
        $gitRoot = $null
        $matches = $false

        if ($exists -and $null -ne $gitCommand) {
            try {
                $found = & $gitCommand.Source -C $checkout rev-parse --show-toplevel 2>$null
                if ($LASTEXITCODE -eq 0 -and $found) {
                    $gitRoot = [System.IO.Path]::GetFullPath(([string]($found | Select-Object -First 1)).Trim())
                    $expected = [System.IO.Path]::GetFullPath($checkout)
                    $matches = [string]::Equals(
                        $gitRoot.TrimEnd('\', '/'),
                        $expected.TrimEnd('\', '/'),
                        [System.StringComparison]::OrdinalIgnoreCase
                    )
                }
            }
            catch {
                $gitRoot = $null
            }
        }

        [pscustomobject]@{
            Name = [string]$entry.name
            Exists = [bool]$exists
            MatchesGitRoot = [bool]$matches
            ReportedRoot = $checkout
            ActualGitRoot = $gitRoot
        }
    }
)

$results
if ($RequireAll -and @($results | Where-Object { -not $_.Exists -or -not $_.MatchesGitRoot }).Count -gt 0) {
    exit 1
}
