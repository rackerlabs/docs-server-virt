.. _understanding-vm-replication-roles-and-responsibilities:



=============================================================
Understanding  VM   replication  roles  and  responsibilities
=============================================================



The following list identifies the roles and responsibilities for
Rackspace Technology VMware Server Virtualization VM replication:

* **Rackspace Technology:** Rackspace Technology is responsible for performing
  the task.
* **Customer:** Customer is responsible for performing the task.
* **Rackspace Technology (Customer Initiated:** Rackspace Technology is
  responsible for performing the task, but we expect the Customer to
  initiate the actions.
* **Not Applicable:** The task or option is not applicable to the selected
  edition.

**Sizing**
+----------------------------------------------------+-----------------------+------------------------+
| **Task**                                           | **LOCAL REPLICATION** | **REMOTE REPLICATION** |
+====================================================+=======================+========================+
| Size customer-required infrastructure for local    | Rackspace             | Rackspace              |
| recoveries or failovers to the target site         |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Provide VM replication journal-sizing requirements | Rackspace             | Rackspace              |
+----------------------------------------------------+-----------------------+------------------------+



**Deployment**
+----------------------------------------------------+-----------------------+------------------------+
| **TASK**                                           | **LOCAL REPLICATION** | **REMOTE REPLICATION** |
+====================================================+=======================+========================+
| Install VM replication management infrastructure   | Rackspace             | Rackspace              |
| at source and target site as needed                |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Pair source and target site as peers as needed     | Not Applicable        | Rackspace              |
+----------------------------------------------------+-----------------------+------------------------+
| Install VM replication virtual replication         | Rackspace             | Rackspace              |
| appliance on every customer-dedicated hypervisor   |                       |                        |
| at source and target site as needed                |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+

**Configuration**
+----------------------------------------------------+-----------------------+------------------------+
| **TASK**                                           | **LOCAL REPLICATION** | **REMOTE REPLICATION** |
+====================================================+=======================+========================+ 
| Configure Rackspace network connection betwee n    | Not Applicable        | Rackspace              |
| source and target site as needed                   |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Configure default Virtual Protection Groups (VPG)  | Rackspace             | Rackspace              |
+----------------------------------------------------+-----------------------+------------------------+
| Customize networking and VPG configuration         | Rackspace             | Rackspace              |
|                                                    | (Customer initiated)  | (Customer initiated)   |
+----------------------------------------------------+-----------------------+------------------------+

**Testing and recovery**
+----------------------------------------------------+-----------------------+------------------------+
| **TASK**                                           | **LOCAL REPLICATION** | **REMOTE REPLICATION** |
+====================================================+=======================+========================+
| Perform failover test operations                   | Rackspace             | Rackspace              |
|                                                    | (Customer initiated)  | (Customer initiated)   |
+----------------------------------------------------+-----------------------+------------------------+
| Perform local recovery operations                  | Rackspace             | Not Applicable         |
|                                                    | (Customer initiated)  |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Perform remove failover and move operations        | Not Applicable        | Rackspace              |
|                                                    |                       | (Customer initiated)   |
+----------------------------------------------------+-----------------------+------------------------+
| Complete database and application recovery after   | Customer              | Customer               |
| recovery or failover operations                    |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Validate VMs are operating as expected after       | Customer              | Customer               |
| recovery or failover operations                    |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Perform failback operations from target site to    | Not Applicable        | Rackspace              |
| source site                                        |                       | (Customer initiated)   |
+----------------------------------------------------+-----------------------+------------------------+

**Monitoring and management**
+----------------------------------------------------+-----------------------+------------------------+
| **TASK**                                           | **LOCAL REPLICATION** | **REMOTE REPLICATION** |
+====================================================+=======================+========================+
| 24 x 7 monitoring of replication and investigate   | Rackspace             | Rackspace              |
| failures between source and target site            |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Perform incident resolution for VM replication     | Rackspace             | Rackspace              |
| management infrastructure                          |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Perform maintenance on VM replication              | Rackspace             | Rackspace              |
| management infrastructure                          |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Perform maintenance on VM replication              | Rackspace             | Rackspace              |
| management infrastructure including replication    |                       |                        |
| software upgrades                                  |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
| Escalation of incidents to technology vendor for   | Rackspace             | Rackspace              |
| software support or on-site resolution             |                       |                        |
+----------------------------------------------------+-----------------------+------------------------+
=======

+-----------------------------------------------------------------------------------------------------------+
| **TASK**                                            | **LOCAL REPLICATION**     | **REMOTE REPLICATION**  |                        
+=====================================================+===========================+=========================+
| Size customer-required infrastructure for local     | Rackspace                 | Rackspace               | 
| recoveries or failovers to the target site          |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Provide VM replication journal-sizing requirements  | Rackspace                 | Rackspace               | 
|                                                     |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+

**Deployment**

+-----------------------------------------------------------------------------------------------------------+
| **TASK**                                            | **LOCAL REPLICATION**     | **REMOTE REPLICATION**  |                        
+=====================================================+===========================+=========================+
| Install VM replication management infrastructure    | Rackspace                 | Rackspace               | 
| at source and target site as needed                 |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Pair source and target site as peers as needed      | Not Applicable            | Rackspace               | 
|                                                     |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Install VM replication virtual replication          | Rackspace                 | Rackspace               | 
| appliance on every customer-dedicated hypervisor    |                           |                         |
| at source and target site as needed                 |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+

**Configuration**

+-----------------------------------------------------------------------------------------------------------+
| **TASK**                                            | **LOCAL REPLICATION**     | **REMOTE REPLICATION**  |                        
+=====================================================+===========================+=========================+
| Configure Rackspace network connection between      | Not Applicable            | Rackspace               | 
| source and target site as needed                    |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Configure default Virtual Protection Groups (VPG)   | Rackspace                 | Rackspace               | 
|                                                     |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Customize networking and VPG configuration          | Rackspace                 | Rackspace               | 
|                                                     | (Customer initiated)      | (Customer initiated)    |
+-----------------------------------------------------+---------------------------+-------------------------+

**Testing and recovery**

+-----------------------------------------------------------------------------------------------------------+
| **TASK**                                            | **LOCAL REPLICATION**     | **REMOTE REPLICATION**  |                        
+=====================================================+===========================+=========================+
| Perform failover test operations                    | Rackspace                 | Rackspace               | 
|                                                     | (Customer initiated)      | (Customer initiated)    |
+-----------------------------------------------------+---------------------------+-------------------------+
| Perform local recovery operations                   | Rackspace                 | Not Applicable          | 
|                                                     | (Customer initiated)      |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Perform remove failover and move operations         | Not Applicable            | Rackspace               | 
|                                                     |                           | (Customer initiated)    |
+-----------------------------------------------------+---------------------------+-------------------------+
| Complete database and application recovery after    | Customer                  | Customer                | 
| recovery or failover operations                     |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Validate VMs are operating as expected after        | Customer                  | Customer                | 
| recovery or failover operations                     |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Perform failback operations from target site to     | Not Applicable            | Rackspace               | 
| source site                                         |                           | (Customer initiated)    |
+-----------------------------------------------------+---------------------------+-------------------------+

**Monitoring and management**

+-----------------------------------------------------------------------------------------------------------+
| **TASK**                                            | **LOCAL REPLICATION**     | **REMOTE REPLICATION**  |                        
+=====================================================+===========================+=========================+
| 24 x 7 monitoring of replication and investigate    | Rackspace                 | Rackspace               | 
| failures between source and target site             |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Perform incident resolution for VM replication      | Rackspace                 | Rackspace               | 
| management infrastructure                           |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Perform maintenance on VM replication               | Rackspace                 | Rackspace               | 
| management infrastructure                           |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Perform maintenance on VM replication               | Rackspace                 | Rackspace               | 
| management infrastructure including replication     |                           |                         |
| software upgrades                                   |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+
| Escalation of incidents to technology vendor for    | Rackspace                 | Rackspace               | 
| software support or on-site resolution              |                           |                         |
+-----------------------------------------------------+---------------------------+-------------------------+























