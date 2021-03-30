.. _understanding-migrations-using-vmotion:


======================================
Understanding migrations
======================================

The following forms of migration are available depending on what you
need to move:

* **vMotion:** vMotion is the technology that we use to migrate a VM from one ESXi host to another ESXi host. Depending on the circumstances, the migration can occur either offline or online. DRS uses vMotion automatically to balance the load between ESXi hosts. This form of migration happens either on a daily basis, often without your awareness as a result of automated action, or because you requested it. See :ref:`migrate-a-vm-to-a-different-esxi-host-by-using-vmotion` for more information.

* **Storage vMotion:** Storage vMotion migrates a VM from one VMFS datastore to another. The target datastore must have sufficient space. Storage vMotion migration can take a long time to complete, so your system might experience performance degradation during the migration operation. See :ref:`move-a-vm-to-a-datastore-by-using-storage-vMotion` for more information.

* **vMotion without Shared Storage:** vMotion without Shared Storage combines vMotion and storage vMotion. vMotion without Shared Storage is most commonly used for migration between two standalone hypervisors. See :ref:`migrate-by-using-vmotion-without-shared-storage` for more information.

* **Initial migration that occurs when you become a Rackspace Technology customer** and migrate an existing workload to Server Virtualization. See :ref:`migrate-a-workload-to-vmware-server-virtualization` for more information about migrating a workload from another environment to Server Virtualization.


