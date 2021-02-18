.. _understanding-vm-recovery-roles-and-responsibilities:

11.2.3.

====================================================
Understanding VM recovery roles and responsibilities
====================================================

The following table identifies the roles and responsibilities for the 
customer and Rackspace Technology.

+---------------+----------------------------------------+--------------------------------------------------+
| Category      | Customer                               | Rackspace Technology                             |                                                     |
+===============+========================================+==================================================+
| Backup        | Defines the backup and recovery        | Implements the appropriate hypervisor proxies,   |    
| delivery of   | requirements for VMs and applications. | VM configuration and application backup agents.  |
+---------------+----------------------------------------+--------------------------------------------------+
| Monitoring    |                                        | Monitors backup operations.                      |    
+---------------+----------------------------------------+--------------------------------------------------+
| Recovery      | Requests full VM, individual file, or  | Performs the recovery.                           |    
|               | application-level recovery as needed.  |                                                  |
+---------------+----------------------------------------+--------------------------------------------------+