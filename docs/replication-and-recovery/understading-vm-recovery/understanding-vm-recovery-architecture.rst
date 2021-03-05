.. _understanding-vm-recovery-architecture:



======================================
Understanding VM recovery architecture
======================================



The following diagram illustrates the architecture of VM recovery:


.. image:: Picture3.png





.. _understanding-vm-recovery-roles-and-responsibilities:




Understanding VM recovery roles and responsibilities
____________________________________________________





The following table identifies the roles and responsibilities for the
customer and Rackspace Technology.

+---------------+----------------------------------------+--------------------------------------------------+
| Category      | Customer                               | Rackspace Technology                             |                                                     |
+===============+========================================+==================================================+
| Backup        | Defines the backup and recovery        | Implements the appropriate hypervisor proxies,   |    
|               | requirements for VMs and applications. | VM configuration and application backup agents.  |
+---------------+----------------------------------------+--------------------------------------------------+
| Monitoring    |                                        | Monitors backup operations.                      |    
+---------------+----------------------------------------+--------------------------------------------------+
| Recovery      | Requests full VM, individual file, or  | Performs the recovery.                           |    
|               | application-level recovery as needed.  |                                                  |
+---------------+----------------------------------------+--------------------------------------------------+








.. _understanding-vm-recovery-technical-requirements-and-limitations:




Understanding VM recovery technical requirements and limitations
________________________________________________________________





VM recovery is subject to the following technical requirements and
limitations:

* Each hypervisor needs a VM recovery proxy.
* VMware datastores containing virtual machines need a minimum of
  15% free space. VM backup jobs are stopped if less than 10% datastore
  space is available.
* Backup and restore times depend on the VM(s) size. VMs larger in size
  and smaller file counts experience a more extended backup and recovery
  time.
* We use client-based data de-duplication in order to reduce backup times.
  
**Note:** If your VMs do not meet these requirements, then consider VM
Replication Local Edition as an option.








