.. _understanding-test-operations:

11.1.7

=============================
Understanding test operations
=============================

You can replace the VM value in the VPG name with a customer-defined name. 
Defining the appendix helps you identify the contents of the VPG.

For example, if you group VMs by customers, use the customer name or ID. 
If you group VMs by application or workload, use a descriptor, such 
as ProdCRM, to represent your Production CRM application.

* **Journal history days:** The target length of time you can roll back VMs 
  within a VPG upon recovery.

  By default, each VM has a value of seven days. Setting the Zerto Journal 
  History to seven days provides the ability to specify a recovery 
  point-in-time within the last seven days.

  For example, if you accidentally decommission the wrong VMs and need to 
  recover the VMs, but it takes you five days to identify the mistake, 
  you can select the checkpoint before the decommission because you have 
  a seven-day journal full of checkpoints.

  **Note:** The actual journal history size depends on the available storage. 
  Configuring longer journal history requires the storage capacity to keep 
  all changes for the desired period. The configured target might not be met 
  and journal checkpoints that have not met the desired journal history 
  target might be automatically deleted if there is insufficient space.

  * **Boot order:** The order in which the VMs contained within a VPG boot 
    upon recovery. VMs boot in ascending order.

    For example, if the VPG includes a database, application tier, and web 
    server tier and the database must be available before the application 
    tier or web server, you can set the database boot order to 1, application 
    tier to 2, and web server to 3.

  * **Use bubble network:** If the VMs are configured to use a bubble network, 
    you can’t access them. However, we verify via console if the OS has booted 
    up successfully. A bubble network is an isolated network which isn’t 
    connected to any other network.

During the test, the source site continues to run normally, and any changes you 
make on the target site are discarded at the end of the test. If you prefer to 
shut down the source VMs and run the VMs on the secondary site, consider a 
planned failover instead.







