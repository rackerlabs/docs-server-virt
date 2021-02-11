.. _manage-vcpu:

9.11

===========
Manage vCPU
===========

It is important that you size the VM’s vCPU correctly. If you assign 
too few vCPUs to a VM, the VM’s performance might suffer. If you assign 
too many vCPUs to a VM, you might create CPU congestion on the hypervisor. 
When you over-allocate vCPUs, the VM can unknowingly share vCPUs with 
other VMs, and the Guest OS might misreport CPU-related metrics.

If you need guidance on how much vCPU to allocate, create a Rackspace Technology 
support ticket that requests a vCPU consultation.

This section includes the following topics:

* Add vCPU
* Remove vCPU
* Adjust the number of virtual sockets and the number of cores per socket
* Set vCPU reservation










