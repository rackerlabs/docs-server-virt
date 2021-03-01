.. _downgrade-vram:


==============
Downgrade vRAM
==============

If your VM consistently underutilizes vRAM resources, the VM might be
unnecessarily wasting physical RAM on the hypervisor. By reducing vRAM,
you free up physical RAM resources for all VMs. While reducing vRAM might
seem counterintuitive, removing vRAM could actually improve the performance
of all VMs running on the hypervisor, including the VM in question.

If you need help determining how much vRAM to remove, create a
Rackspace Technology ticket, and we’ll run a report against your environment
and provide a recommendation.

To downgrade vRAM, refer to :ref:`resize-a-vm`.



