.. _resize-a-vm:

9.8

===========
Resize a VM
===========

A VMware snapshot is a copy of the VM’s disk file (VMDK) at a given point 
in time. Snapshots provide a changelog for the virtual disk, and you can 
use them to restore a VM to a particular point in time when a failure or 
system error occurs.

Snapshot files that grow can affect VMs on the hypervisor. For this reason, 
we recommend keeping a snapshot for no longer than two days. 
After this time, you can delete the snapshot or revert to the snapshot and 
original disks.

This section includes the following topics:
* Create a snapshot
* Delete a snapshot
* Revert to a snapshot
















