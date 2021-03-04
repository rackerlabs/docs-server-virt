.. _understanding-vram:



==================
Understanding vRam
==================

You can allocate physical RAM on the hypervisor to the VMs as
virtual RAM (vRAM). If you allocate more vRAM than is physically
installed, application performance can suffer because of the techniques
that ESXi uses to reclaim memory, such as memory swapping and memory
ballooning.

You should only allocate as many vRAM resources as your VM needs.

