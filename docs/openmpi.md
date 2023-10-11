# Bug with openmpi4 with omni-path

There is a bug in openmpi4 with omni-path that when using more than one node
and more tasks per node than what is half of available cpus
following type of error will be printed:

```
kuutti2-compute-2.novalocal.498516PSM2 can't open hfi unit: -1 (err=23)
kuutti2-compute-2.novalocal.498517hfi_userinit_internal: Warning: assign_context command failed: Device or resource busy
kuutti2-compute-2.novalocal.498517hfp_gen1_context_open: hfi_userinit_internal: failed, trying again (1/3)
kuutti2-compute-2.novalocal.498517hfi_userinit_internal: Warning: assign_context command failed: Device or resource busy
kuutti2-compute-2.novalocal.498517hfp_gen1_context_open: hfi_userinit_internal: failed, trying again (2/3)
kuutti2-compute-2.novalocal.498517hfi_userinit_internal: Warning: assign_context command failed: Device or resource busy
kuutti2-compute-2.novalocal.498517hfp_gen1_context_open: hfi_userinit_internal: failed, trying again (3/3)
kuutti2-compute-2.novalocal.498517hfi_userinit_internal: Warning: assign_context command failed: Device or resource busy
```

More information and possible workaround ca be found on [this](https://github.com/open-mpi/ompi/issues/9575) openmpi github issue.

[This](https://github.com/open-mpi/ompi/issues/10601) also might be related.
