# Local development port matrix (as supplied / updated)

| Local app | URL | Evidence |
| --- | --- | --- |
| Ekole Québec learner portal | `http://127.0.0.1:8765/` and `/eleve/` | `ekole-quebec/LANCER_EKOLE_QUEBEC.bat` |
| Ekole Québec teacher editor | `http://127.0.0.1:8766/` | Same Québec launcher |
| Ekole Pastorale learner portal | `http://127.0.0.1:8775/` | `ecole-pastorale/LANCER_PASTORALE.bat` |
| Ekole Pastorale teacher editor | `http://127.0.0.1:8776/` | Same pastoral launcher |
| Ékole OpsConsole | `http://127.0.0.1:8766/` | Ékole `opsconsole/README.md`, `opsconsole/ekole_ops.py` |
| Skope | `http://127.0.0.1:8767/` | Updated Skope `skope/config.py` default |

**Coexistence warning:** Enseignant and OpsConsole both default to `8766`; launching both with their defaults will collide. This update **does not patch Ékole**, only records the conflict. Skope supports `--port` override, e.g. `py -3 -m skope demo --port 8790`.

Commands:

```powershell
# Skope, from its repository root
py -3 -m skope demo
# Open http://127.0.0.1:8767/

# Ekole Core, from its checkout. Choose one pack explicitly.
py -3 launcher.py --contenu ..\ekole-quebec --ouvrir
# For the pastoral pack, use its launcher to select ports 8775/8776.
..\ecole-pastorale\LANCER_PASTORALE.bat

# To use OpsConsole, avoid running Ékole Enseignant on the same default port
py -3 opsconsole\ekole_ops.py
# Open http://127.0.0.1:8766/
```

This is **developer-local** addressing, not network deployment, Koali onboarding, OIDC integration or public routing.
