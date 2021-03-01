.. _shrink-vdisk:


============
Shrink vDisk
============

We cannot shrink a vDisk. If you require a smaller vDisk, complete any of
the following procedures.

For vDisks that serve as a non-system partition, complete the following
steps:

1. Request that we add a smaller vDisk to a datastore.:ref:`add-vdisk`.
2. Request that we migrate your data from the larger vDisk to the smaller
   vDisk.
3. Request that we delete the larger vDisk:ref:`delete-vdisk`.

For vDisks that serve as a system partition in the OS, you can request 
that we reimage your VM, or you can complete the following steps:

1. Order a VM :ref:`order-a-vm`.
2. Request that we migrate your data to the new VM.
3. Request that we decommission the old VM.
