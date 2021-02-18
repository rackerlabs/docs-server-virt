.. _move-a-vm-between-two-hosts-or-two-datastores:

9.13

=============================================
Move a VM between two hosts or two datastores
=============================================

There are three methods of migrating a VM from one host or datastore 
to another host or datastore within the VMware Server Virtualization 
environment.

* **vMotion:** vMotion migrates a VM from one ESXi host to another ESXi host. 
  Depending on the circumstances, the migration can occur either 
  offline or online. 

* **Storage vMotion:** Storage vMotion migrates a VM from one VMFS datastore 
  to another VMFS datastore.

* **vMotion without Shared Storage:** vMotion without Shared Storage combines 
  vMotion and storage vMotion. vMotion without Shared Storage is most commonly 
  used for migration between two standalone hypervisors.

This section includes the following topics:

* Migrate a VM to a different ESXi host by using vMotion
* Move a VM to a datastore by using storage vMotion
* Migrate by using vMotion without shared storage
