# Operations — release and activation

## Platform release model

kOA-Linux separates `system`, `services`, `governance` and `knowledge` release channels and binds compatible versions through Release Sets.

A Release Set is authoritative for platform release compatibility, not for Kristal epistemic validation or Runtime Pack active state.

## Runtime Pack activation

For a kOA-Linux Runtime Pack:

1. artifact arrives through the `knowledge` release channel;
2. Release Set compatibility is checked where required;
3. `kristal_runtime` validates schema/identity/digest/provenance/trust/compatibility/channel/downgrade/substitution policy;
4. `kristal_runtime` owns activation eligibility and active Runtime Pack state;
5. kOA Node Agent executes the narrow privileged transition when required;
6. owner receipts/evidence are emitted.

The deprecated Digital Ecosystem Release Record and Runtime Activation State are not authorities.
