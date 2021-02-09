.. _understanding_roles_and_responsibilities:

4

========================================
Understanding roles and responsibilities
========================================

Your VMware Server Virtualization environments can comprise both 
supported and unsupported Guest OSs.

* **Supported OS:** A Guest OS that is supported by Rackspace.
* **Unsupported OS:** A Guest OS that is not supported by Rackspace 
and that requires you to assume some responsibility for that managed VM.

The following table lists all services and the party responsible for 
managing them. For some tasks, you and Rackspace Technology share responsibility.

+---------------+-----------------------------------------------------------------------------------+
|               | Layer                                                                             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Service       | Physical    | ESXi        | VM          | Managed     | Managed     | Application |
|               | server      |             | Container   | VM          | VM          |             |
|               |             |             |             | Supported   | Unsupported |             |
|               |             |             |             | OS          | OS          |             |
+===============+=============+=============+=============+=============+=============+=============+
| **Provisioning**                                                                                  |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Manage        | Rackspace   | N/A         | N/A         | N/A         | N/A         | N/A         | 
| delivery of   |             |             |             |             |             |             |
| equipment     |             |             |             |             |             |             |
| (as needed)   |             |             |             |             |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Rackspace     | Rackspace   | Rackspace   | Rackspace   | Rackspace   | Customer    | Depends     |
| provided      |             |             |             |             |             |             |
| guest OS      |             |             |             |             |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Customer-     | Rackspace   | Rackspace   | Rackspace   | Customer    | Customer    | Depends     |
| provided      |             |             |             |             |             |             |
| guest         |             |             |             |             |             |             |
| OS            |             |             |             |             |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Initial       | Rackspace   | Rackspace   | Rackspace   | Customer    | Customer    | Depends     |
| deployment    |             |             |             |             |             | on          |
|               |             |             |             |             |             | application |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| **Alerting**                                                                                      |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Performance   | Rackspace   | Rackspace   | Rackspace   | Rackspace   | Customer    | Customer    |
| monitoring    | Reactive    | Reactive    | Reactive    | Reactive    |             |             |
|               | Only        | Only        | Only        | Only        |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Outage        | Rackspace   | Rackspace   | No          | Rackspace   | Customer    | Customer    |
| monitoring    | Reactive    | Reactive    |             | Reactive    |             |             |
|               | Only        | Only        |             | Only        |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| **Reporting**                                                                                     |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Performance   | Customer-   | Customer-   | Customer-   | Customer-   | Customer-   | Customer-   |
| reports       | specific    | specific    | specific    | specific    | specific    | specific    |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Outage        | Customer-   | Customer-   | Customer-   | Customer-   | Customer-   | Customer-   |
| reports       | specific    | specific    | specific    | specific    | specific    | specific    |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Bandwith      | Rackspace   | N/A         | Rackspace   | N/A         | N/A         | N/A         |
| consumption   |             |             | Per         |             |             |             |
| reporting     |             |             | request     |             |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| **Access**                                                                                        |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Physical      | Rackspace   | N/A         | N/A         | N/A         | N/A         | N/A         |
| Access        |             |             |             |             |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Remote/       | Rackspace   | Rackspace   | Rackspace   | Rackspace   | Customer    | Same        |
| Logical       |             |             |             | and         |             | as          |
| Access        |             |             |             | Customer    |             | OS          |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Administrator | Rackspace   | Rackspace   | Rackspace   | Rackspace   | Customer    | N/A         |
| Root          |             |             |             | and         |             |             |
| access        |             |             |             | Customer    |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| **Change management**                                                                             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Patching      | Rackspace   | Rackspace   | Rackspace   | Rackspace   | Customer    | Customer    |
|               | coordinated | coordinated | coordinated | coordinated |             | unless      |
|               | with        | with        | with        | with        |             | application |           
|               | Customer    | Customer    | Customer    | Customer    |             | services    |
|               |             |             |             |             |             | purchased   |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Hardware      | Rackspace   | N/A         | Rackspace   | Rackspace   | Customer    | Customer    |
| changes,      | per         |             | per         | per         |             |             |
| including     | request     |             | request     | request     |             |             |           
| software      | (Fee)       |             | (Fee)       | (Fee)       |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Password      | Rackspace   | N/A         | N/A         | Rackspace   | N/A         | N/A         |
| rotation for  |             |             |             |             |             |             |     
| Rackspace     |             |             |             |             |             |             |
| credentials   |             |             |             |             |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
| Scheduled     | Rackspace   | Rackspace   | Rackspace   | Rackspace   | Customer    | Customer    |
| maintenances  | coordinated | coordinated | coordinated | coordinated |             |             |
|               | with        | with        | with        | with        |             |             |
|               | Customer    | Customer    | Customer    | Customer    |             |             |
+---------------+-------------+-------------+-------------+-------------+-------------+-------------+








