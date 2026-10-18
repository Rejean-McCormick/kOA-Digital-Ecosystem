#Requires -Version 5.1
<#
.SYNOPSIS
  Remplacement ponctuel de SenTient/main après sauvegarde de origin/main.
.DESCRIPTION
  OPÉRATION DESTRUCTIVE : ne jamais lancer depuis GitSink.bat / Runner V8.
  Vérifie l'URL directe, l'arbre propre, crée une sauvegarde locale et une branche
  de sauvegarde SUR GITHUB avant de proposer un push avec bail explicite SHA.
#>
[CmdletBinding()]
param([string]$RepoPath = 'C:\mycode\SenTient\SenTient')

$ErrorActionPreference = 'Stop'
$expectedUrl = 'https://github.com/Rejean-McCormick/SenTient.git'

function GitOrFail {
    param([Parameter(Mandatory=$true)][string[]]$GitArgs)
    # PowerShell 5.1 peut traiter les messages stderr natifs (même informatifs)
    # comme des erreurs ; le véritable résultat est le code de sortie Git.
    $ErrorActionPreference = 'Continue'
    $out = & git -C $RepoPath @GitArgs 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Git a échoué : git $($GitArgs -join ' ')`n$($out -join "`n")"
    }
    return $out
}

try {
    if (-not (Test-Path -LiteralPath $RepoPath -PathType Container)) {
        throw "Le répertoire est introuvable : $RepoPath"
    }
    $root = (GitOrFail -GitArgs @('rev-parse','--show-toplevel') | Select-Object -First 1).Trim()
    if ([IO.Path]::GetFullPath($root).TrimEnd('\','/') -ine [IO.Path]::GetFullPath($RepoPath).TrimEnd('\','/')) {
        throw 'Le chemin indiqué ne correspond pas à la racine Git.'
    }
    $originConfigured = (GitOrFail -GitArgs @('config','--get','remote.origin.url') | Select-Object -First 1).Trim()
    $originResolved = (GitOrFail -GitArgs @('remote','get-url','origin') | Select-Object -First 1).Trim()
    $pushResolved = (GitOrFail -GitArgs @('remote','get-url','--push','origin') | Select-Object -First 1).Trim()
    if ($originConfigured -cne $expectedUrl -or $originResolved -cne $expectedUrl -or $pushResolved -cne $expectedUrl) {
        throw "Remote non canonique ou réécrite. URL attendue : $expectedUrl"
    }
    $branch = (GitOrFail -GitArgs @('symbolic-ref','--short','HEAD') | Select-Object -First 1).Trim()
    if ($branch -cne 'main') { throw "Branche actuelle : $branch ; main requis." }
    $dirty = GitOrFail -GitArgs @('status','--porcelain=v1')
    if ($dirty) { throw 'Arbre de travail non propre : examiner/committer/stasher les changements avant de continuer.' }
    $localSha = (GitOrFail -GitArgs @('rev-parse','refs/heads/main') | Select-Object -First 1).Trim()
    # Ne réécrit jamais l'arbre de travail; seul .git est rafraîchi.
    [void](GitOrFail -GitArgs @('fetch','--no-tags','origin','+refs/heads/main:refs/remotes/origin/main'))
    $remoteSha = (GitOrFail -GitArgs @('rev-parse','refs/remotes/origin/main') | Select-Object -First 1).Trim()
    Write-Host "Local main :   $localSha"
    Write-Host "GitHub main :  $remoteSha"
    Write-Host 'Commits présents uniquement sur une des deux branches :'
    GitOrFail -GitArgs @('log','--oneline','--left-right','--max-count=30',("{0}...{1}" -f 'main',$remoteSha)) | ForEach-Object { Write-Host $_ }
    if ($localSha -ceq $remoteSha) {
        Write-Host 'Aucune divergence : main est déjà aligné. Aucun push forcé.'
        exit 0
    }
    & git -C $RepoPath merge-base --is-ancestor $remoteSha $localSha
    if ($LASTEXITCODE -eq 0) {
        Write-Host 'Le distant est un ancêtre de main : préférer un push normal, aucun push forcé.'
        exit 0
    }
    if ($LASTEXITCODE -ne 1) { throw 'Impossible de comparer les historiques main/origin.' }
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $backupBranch = 'backup/sentient-remote-' + $stamp
    $backupRef = 'refs/heads/' + $backupBranch
    [void](GitOrFail -GitArgs @('branch',$backupBranch,$remoteSha))
    Write-Host "Sauvegarde locale créée : $backupBranch"
    # Ref distante visible sous GitHub: préserve l'ancien main même si ce PC est perdu.
    [void](GitOrFail -GitArgs @('push','origin',("{0}:{1}" -f $remoteSha,$backupRef)))
    Write-Host "Sauvegarde distante créée : $backupRef"
    $remoteBackupSha = (GitOrFail -GitArgs @('ls-remote','--exit-code','origin',$backupRef) | Select-Object -First 1).Split("`t")[0]
    if ($remoteBackupSha -cne $remoteSha) { throw 'La sauvegarde distante est introuvable ou son SHA est inattendu. Aucun remplacement.' }
    Write-Warning "Les commits GitHub propres à main ne seront plus visibles sur main après le push. Sauvegarde : $backupRef ($remoteSha)."
    $confirmation = Read-Host 'Saisis exactement FORCER SENTIENT pour remplacer GitHub/main par le main local'
    if ($confirmation -cne 'FORCER SENTIENT') {
        Write-Host "Annulé. La sauvegarde a été créée, mais main n'a pas été remplacé."
        exit 1
    }
    # Lease explicit et figé : ne remplace main que si le distant n'a pas bougé depuis le fetch.
    [void](GitOrFail -GitArgs @('push',("--force-with-lease=refs/heads/main:{0}" -f $remoteSha), 'origin', 'refs/heads/main:refs/heads/main'))
    Write-Host 'SenTient/main remplacé. Vérifier via fetch et rev-parse origin/main.'
} catch {
    [Console]::Error.WriteLine($_.ToString())
    exit 2
}
