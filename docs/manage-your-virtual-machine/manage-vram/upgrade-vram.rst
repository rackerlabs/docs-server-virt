.. _upgrade-vram:



============
Upgrade vRAM
============



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

