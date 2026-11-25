<#
.SYNOPSIS
Read-only V5.13 audit of local canonical Kristals against public projection.
.DESCRIPTION
No edits to either tree. Never stages or publishes. Optional private report is
written only through the Manager's path-guarded new-file API.
#>
param(
    [string]$Locals = 'C:\mycode\Kristal\locals',
    [string]$Public = 'C:\mycode\Kristal\kristal-public',
    [string]$Manager = 'C:\mycode\Kristal\Kristal-Manager',
    [string]$Output
)

$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7+ required.' }
foreach ($entry in @{'Locals' = $Locals; 'Public' = $Public; 'Manager' = $Manager}.GetEnumerator()) {
    if (!(Test-Path -LiteralPath $entry.Value -PathType Container)) {
        throw "Directory not found: $($entry.Key) : $($entry.Value)"
    }
}
if (!(Test-Path -LiteralPath (Join-Path $Manager 'kristal_manager\local_first_audit.py') -PathType Leaf)) {
    throw 'Manager V5.13 overlay missing. First run installer audit, then -Apply.'
}
if (!(Test-Path -LiteralPath (Join-Path $Public 'kristals\index.json') -PathType Leaf)) {
    throw 'Public collection index missing. No changes made.'
}

$oldPythonPath = $env:PYTHONPATH
try {
    $env:PYTHONPATH = $Manager
    if ($oldPythonPath) { $env:PYTHONPATH += [IO.Path]::PathSeparator + $oldPythonPath }
    $arguments = @('-m', 'kristal_manager', 'audit-local-public', '--locals', $Locals, '--public', $Public)
    if ($Output) { $arguments += @('--output', $Output) }
    & python @arguments
    if ($LASTEXITCODE -ne 0) {
        if ($Output -and (Test-Path -LiteralPath $Output -PathType Leaf)) {
            Write-Warning "Audit report saved for review: $Output"
        }
        throw "Local-first audit blocked (exit $LASTEXITCODE). Neither canon nor public was modified."
    }
    Write-Host 'V5.13 INTEGRITY PASS — OBSERVATION ONLY; publication non autorisée.' -ForegroundColor Green
}
finally {
    $env:PYTHONPATH = $oldPythonPath
}
