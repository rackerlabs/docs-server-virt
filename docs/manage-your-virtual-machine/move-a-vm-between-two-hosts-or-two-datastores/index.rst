.. _move-a-vm-between-two-hosts-or-two-datastores:



=============================================
Move a VM between two hosts or two datastores
=============================================

There are three methods of migrating a VM from one host or datastore
to another host or datastore within the VMware Server Virtualization 
environment.

* **vMotion:** vMotion migrates a VM from one ESXi host to another
  ESXi host. Depending on the circumstances, the migration can occur
  either offline or online.

* **Storage vMotion:** Storage vMotion migrates a VM from one VMFS
  datastore to another VMFS datastore.

* **vMotion without Shared Storage:** vMotion without Shared Storage
  combines vMotion and storage vMotion. vMotion without Shared Storage is
  most commonly used for migration between two standalone hypervisors.

This section includes the following topics:

- :ref:`Migrate a VM to a different ESXi host by using vMotion <migrate-a-vm-to-a-different-esxi-host-by-using-vmotion>`
- :ref:`Move a VM to a datastore by using storage vMotion <move-a-vm-to-a-datastore-by-using-storage-vmotion>`
- :ref:`Migrate by using vMotion without shared storage <migrate-by-using-vmotion-without-shared-storage>`



  .. toctree::
   :maxdepth: 2
   :hidden:

   
   migrate-a-vm-to-a-different-esxi-host-by-using-vmotion.rst
   move-a-vm-to-a-datastore-by-using-storage-vmotion.rst
   migrate-by-using-vmotion-without-shared-storage.rst

