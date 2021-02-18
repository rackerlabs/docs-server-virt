.. _add-a-resource-pool:

10.1.5

===================
Add a resource pool
===================

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
