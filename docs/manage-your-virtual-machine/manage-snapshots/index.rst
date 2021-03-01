.. _manage-snapshots:


================
Manage snapshots
================

A VMware snapshot is a copy of the VM’s disk file (VMDK) at a given point
in time. Snapshots provide a changelog for the virtual disk, and you can
use them to restore a VM to a particular point in time when a failure or 
system error occurs.

Snapshot files that grow can affect VMs on the hypervisor.
For this reason, we recommend keeping a snapshot for no longer
than two days. After this time, you can delete the snapshot or revert to
the snapshot and original disks.

This section includes the following topics:

- :ref:`Create a snapshot <create-a-snapshot>`
- :ref:`Delete a snapshot <delete-a-snapshot>`
- :ref:`Revert to a snapshot <revert-to-a-snapshot>`


.. toctree::
   :maxdepth: 2
   :hidden:

   
   create-a-snapshot.rst
   delete-a-snapshot.rst
   revert-to-a-snapshot.rst

