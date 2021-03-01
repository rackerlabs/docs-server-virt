.. _add-vdisk:



=========
Add vDisk
=========

If you need an additional disk to store your files, you can
request that we add a vDisk to a VM. When we add a vDisk for you,
we must specify the location. For example, specify the datastore on
which the vDisk is stored. A single vDisk must reside on one datastore.
However, multiple vDisks belonging to the same VM might not necessarily
reside on the same datastore. With that in mind, consider that different
datastores might differ both in performance and free capacity.

If you request that we add a vDisk shared between two VMs (as is the case
with Microsoft clusters), we add the vDisk in the form of an RDM LUN instead.

Before you request Rackspace to add a vDisk, ensure that you have sufficient
free space (excluding reservation) on the datastore where you want to
place the vDisk.

To add a vDisk to your VM, create a Rackspace Technology ticket that
includes the following information:

* The name of the VM.
* The vDisk size.
* The name of the datastore.
* If Rackspace manages the OS, include the drive letter or partition.



