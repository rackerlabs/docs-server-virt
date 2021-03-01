.. _configure-high-availability:


===========================
Configure high availability
===========================



High availability (HA) is a feature that ensures system uptime to an
agreed-upon level.

VMware vSphere® High Availability monitors the ESXi host status, and
when a host fails, the vSphere HA feature automatically restarts
the VMs on remaining hosts.

To configure or modify high availability, open a Rackspace Technology
ticket and specify the HA action you want us to take, including:

* Enable or disable HA and include the cluster name.
* Set up VM overrides for HA
  **Note:** Provide us with the VM name and the HA override setting
  you want to apply to the VM.




.. _distributed-power-management:




Distributed power management
____________________________________________



Rackspace Server Virtualization does not support distributed
power management.



.. _add-a-resource-pool:




Add a resource pool
___________________


Use a resource pool to more granularly define how a VM uses CPU and RAM
resources. For example, we can define shares and limits for a
resource pool. VMs placed in a resource pool are then jointly subject to
these shares and limits.

Resource pools can sometimes produce undesired results. For example, if
you define a high-performance resource pool and then add many VMs to
that pool, the resources required by the VMs are higher than the proportion
of shares or limits available to the pool. Despite your intention to create
a high-performance pool, the VMs in that pool might perform worse than VMs
outside the pool.

If you want to set up a resource pool, open a Rackspace Technology ticket
and request a consultation.






