# Trust and authority boundaries

Identity, authentication, policy authorization, resource admission, artifact verification, epistemic validation/recognition, release compatibility, privileged host operation and presentation state are distinct.

## Cross-system protocol
Where IK is adopted, the receiver authenticates/authorizes/adopts locally. IK admission is not Kristal validation and does not replace platform admission.

## kOA-Linux release boundary
Release Set/channel compatibility is a platform release decision. It does not make an artifact epistemically valid or active.

## Runtime Pack boundary
`kristal_runtime` verifies/adopts the candidate and owns active Runtime Pack state. Required trust, compatibility, channel, downgrade/substitution and other checks fail closed for activation eligibility.

## Privileged host boundary
kOA Node Agent executes only narrow authorized node-local transitions. Successful authorization/resource admission does not by itself mean the active Runtime Pack record changed.

## Koali boundary
Presentation registration, rendering, readiness and Space activation do not grant product authorization, Kristal authority or host privilege.
