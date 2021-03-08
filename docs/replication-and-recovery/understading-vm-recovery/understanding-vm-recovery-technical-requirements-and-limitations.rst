.. _understanding-vm-recovery-technical-requirements-and-limitations:

================================================================
Understanding VM recovery technical requirements and limitations
================================================================


VM recovery is subject to the following technical requirements and
limitations:

* Each hypervisor needs a VM recovery proxy.
* VMware datastores containing virtual machines need a minimum of 15%
  free space. VM backup jobs are stopped if less than 10% datastore
  space is available.
* Backup and restore times depend on the VM(s) size. VMs larger in size
  and smaller file counts experience a more extended backup and
  recovery time.
* We use client-based data de-duplication in order to reduce backup times.

**Note:** If your VMs do not meet these requirements, then consider
VM Replication Local Edition as an option.


