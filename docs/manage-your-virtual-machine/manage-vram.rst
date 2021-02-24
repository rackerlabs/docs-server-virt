.. _manage-vram:



================
Manage vRAM
================

You can allocate physical RAM on the hypervisor to the VMs as vRAM.

Refer to the following topics to manage vRAM on your VM:

* Upgrade vRAM
* Downgrade vRAM
* Set vRAM reservation
* Change vSwap file location


.. _upgrade-vram:




Upgrade vRAM
____________



If your VM consistently consumes all RAM resources and VM performance
suffers, the VM might benefit from additional vRAM.

Consider the following guidelines when you decide to add vRAM:

* Be careful when adding vRAM to your VM. The RAM resources ultimately
  come from the physical hardware, and if the hypervisor is already under
  pressure for RAM, adding RAM might not solve the problem.
* Only allocate as much vRAM as the VM needs.
* When the vRAM allocation approaches or exceeds the amount of
  physical RAM, the ESXi server invokes memory reclamation techniques,
  such as ballooning and swapping. Memory reclamation technologies enable
  slight over-allocation but can adversely affect the performance of the
  target VM and all other VMs on the hypervisor.

If you need help determining how much vRAM to add, contact your
Rackspace Technology account team.

To upgrade vRAM, refer to :ref:`resize-a-vm`.



.. _downgrade-vram:


Downgrade vRAM
______________

If your VM consistently underutilizes vRAM resources, the VM might be
unnecessarily wasting physical RAM on the hypervisor. By reducing vRAM,
you free up physical RAM resources for all VMs. While reducing vRAM might
seem counterintuitive, removing vRAM could actually improve the performance
of all VMs running on the hypervisor, including the VM in question.

If you need help determining how much vRAM to remove, create a
Rackspace Technology ticket, and we’ll run a report against your environment
and provide a recommendation.

To downgrade vRAM, refer to :ref:`resize-a-vm`.



.. _set-vram-reservation:


Set vRam reservation
____________________

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

* The VM name.
* Optionally, the reservation value in GB/MB.
  
To reserve 100% of the vRAM, you do not need to provide a reservation value.





.. _change-vswap-file-location:



Change vSwap file location
__________________________


So that the hypervisor can manage RAM contention, by default,
the hypervisor stores the VM’s memory in a vSwap file located on
the same datastore as the VM. In most cases, the size of this file is
equal to the size of configured vRAM, unless vRAM is reserved.

If you think you want to change the vSwap file location, open a
Rackspace Technology ticket and request a consultation.





