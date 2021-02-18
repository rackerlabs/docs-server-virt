.. _add-vcpu:

9.11.1

===========
Add vCPU
===========

If your VM consistently consumes all CPU resources and performance 
suffers, the VM might benefit from additional vCPUs.

Consider the following guidelines when deciding to add vCPUs: 

* Be careful when adding vCPUs to your VM. The CPU resources come from 
  the physical hardware, and if the hypervisor is already under 
  high demand for CPU, adding vCPU might not solve the problem.
* Only allocate as much vCPU as the VM needs. 
* All vCPUs are scheduled on the physical CPU, even if the OS is not 
  actively using those vCPUs. Over-allocating vCPUs can introduce 
  CPU contention on the hypervisor layer, which can adversely affect 
  the performance of the target VM and all other VMs on the hypervisor.

If you require assistance determining how many vCPUs to add, contact your Rackspace Technology account team.

To add vCPU, refer to Resize a VM.[link]













