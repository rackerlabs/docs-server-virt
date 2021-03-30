.. _set-vram-reservation:


====================
Set vRAM reservation
====================

An application vendor might recommend that you reserve RAM resources if
you are running the application in a virtualized environment.

Reserving vRAM guarantees that physical RAM resources are available
for the VM, which means that the VM does not compete for resources with
other VMs. You should only reserve vRAM when required because reserving
RAM resources means that other VMs on the hypervisor cannot request those
same resources. Failure to get resources they need might adversely
impact those other VMs.

To reserve vRAM, open a Rackspace Technology ticket and provide the
following information:

* The VM name
* Optionally, the reservation value in GB/MB
  
To reserve 100% of the vRAM, you do not need to provide a reservation value.

