.. _understanding_server_virtualization:

2

===================================
Understanding Server Virtualization
===================================

A virtual server runs inside a virtual machine (VM) instead of a physical machine. 
In VMs, the operating system (OS) layer does not link directly to the physical 
hardware layer. Instead, there is a layer between the OS and the physical layer, 
called a virtualization layer. A virtualization layer is sometimes known as an 
abstraction layer because it abstracts hardware from the OS. 

You can run multiple VMs on a single server chassis. This configuration provides 
many benefits, including cost-effectiveness due to consolidation, less machine 
down-time, better resiliency, extra features such as snapshots, and easier migration 
and upgrades.

This chapter explains the following virtualization on VMware concepts:

- What is a virtual machine?
- Understanding hypervisors
- Understanding VMware vSphere clusters
- Understanding VMware vCenter
- Understanding vCPU
- Understanding vRAM
- Understanding networking
- Understanding storage
- Understanding snapshots
- Understanding migrations using vMotion

.. toctree::
   :maxdepth: 2

   request-maintenance.rst
   identify-deployment.rst
   high-volume-events.rst
   resolve-emergency.rst
