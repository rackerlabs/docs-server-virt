.. _detach-vdisk:


============
Detach vDisk
============

Detaching a vDisk removes the vDisk from the VM but keeps the vDisk file
on the datastore. You can reattach the vDisk to the same VM or another VM.

Detaching a vDisk should be temporary. Long-term detachment creates orphaned
vDisks that we might delete when you decommission a VM that we suspect
is related to the orphaned vDisks.

Before you request that we detach a vDisk, ensure that the OS volume on
the vDisk is offline.

To detach a vDisk from your VM, create a Rackspace Technology ticket that
includes the following information:

* The name of the VM
* The vDisk number
* The vDisk size
* The name of the datastore
* If Rackspace Technology manages the OS, include the drive letter or
partition.
