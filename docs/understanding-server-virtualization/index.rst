.. _understanding_server_virtualization:



===================================
Understanding Server Virtualization
===================================

A virtual server runs inside a virtual machine (VM) instead of a physical
machine. In VMs, the operating system (OS) layer does not link directly
to the physical hardware layer. Instead, there is a layer between the OS
and the physical layer, called a virtualization layer. A virtualization
layer is sometimes known as an abstraction layer because it abstracts
hardware from the OS.

You can run multiple VMs on a single server chassis. This configuration
provides many benefits, including cost-effectiveness due to consolidation,
less machine down-time, better resiliency, extra features such as snapshots,
and easier migration and upgrades.

This chapter explains the following virtualization on VMware concepts:


.. toctree::
   :maxdepth: 2

   what-is-a-virtual-machine.rst
   understanding-hypervisors.rst
   understanding-vmware-vsphere-clusters.rst
   understanding-vmware-vcenter.rst
   understanding-vcpu.rst
   understanding-vram.rst
   understanding-networking.rst
   understanding-storage.rst
   understanding-snapshots.rst
   understanding-migrations-using-vmotion.rst
