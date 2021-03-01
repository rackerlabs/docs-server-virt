.. _set-vcpu-reservation:


====================
Set vCPU reservation
====================

An application vendor might recommend that you reserve CPU resources
if you are running the application in a virtualized environment.

Reserving vCPU guarantees that physical CPU resources are available for
the VM, which means that the VM does not compete for resources with
other VMs. You should only reserve vCPU when required because reserving
CPU resources means that other VMs on the hypervisor cannot request
those same resources. Failure to get resources they need might adversely
impact those other VMs.

To reserve vCPU, open a Rackspace Technology ticket and provide the
following information:

* The VM Name.
* Optionally, the reservation value in MHz / GHz.
  
To reserve 100% of the vCPU, you don’t need to specify the reservation
value. We can calculate the MHz / GHz value for you.
