# Implementer guide

Implementers should preserve these separations:

```text
transport/delivery status ≠ domain status
domain status             ≠ epistemic status
compile                    ≠ validate
validate                   ≠ recognize
publish                    ≠ activate
```

## Orgo implementers

Reuse Signal/Workflow/Case/Task and IntegrationOperation/outbox infrastructure. Do not absorb provider models into Orgo core.

## Konnaxion implementers

Keep source events/readings/DecisionRecord in Konnaxion. Cross-system adapters should use explicit boundaries and must not write Orgo/Kristal/kOA-Linux stores directly.

## Da’at/Kristal implementers

Emit Structured Epistemic State or explicitly supported Kristal-native inputs. Never treat validation as a universal compile blocker. Keep source artifact status and recognition metadata explicit.

## Runtime/platform implementers

Provide one authoritative activation state, atomic activation, deterministic rollback, revocation/downgrade checks and complete evidence.
