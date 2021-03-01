.. _delete-vdisk:



============
Delete vDisk
============


A vDisk is a virtual disk that the Guest OS uses for storage as it would
use a physical disk. A vDisk is represented as a **.vmdk** file on a VMFS
datastore.

While you cannot manage a vDisk yourself, we provide a list of information
for the following tasks, which you should include in your ticket so that
we can expedite your request.

This section includes the following topics:

* Add vDisk
* Delete vDisk
* Detach vDisk
* Expand vDisk
* Shrink vDisk




.. _detach-vdisk:



Detach vDisk
____________

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


.. _expand-vdisk:



Expand vDisk
____________

If your environment runs low on free space or you anticipate growth,
you can request that we expand a vDisk.

Before you request that we expand a vDisk, view your
hypervisor configurations [link] to ensure that the datastore on which
the vDisk resides has sufficient free space for expansion, excluding
reservation. If required, we can migrate the vDisk to a datastore that
provides more space. For more information about migrating to a datastore,
refer to Move a VM to a datastore [link] by using storage vMotion.

To expand a vDisk, create a Rackspace Technology ticket that includes the
following information:

* The name of the VM
* The vDisk number
* The current vDisk size and the amount of space you want to add
* If Rackspace Technology manages the OS, include the drive letter or
  partition.

.. _shrink-vdisk:


Shrink vDisk
____________

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
























