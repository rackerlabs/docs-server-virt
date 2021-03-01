.. _manage-vcpu:


===========
Manage vCPU
===========

It is important that you size the VM’s vCPU correctly. If you assign
too few vCPUs to a VM, the VM’s performance might suffer. If you assign
too many vCPUs to a VM, you might create CPU congestion on the hypervisor.
When you over-allocate vCPUs, the VM can unknowingly share vCPUs with
other VMs, and the Guest OS might misreport CPU-related metrics.

If you need guidance on how much vCPU to allocate, create
a Rackspace Technology support ticket that requests a vCPU consultation.

This section includes the following topics:

- :ref:`Add vCPU <add-vcpu>`
- :ref:`Remove vCPU <remove-vcpu>`
- :ref:`Adjust the number of virtual sockets and the number of cores 
  per socket <adjust-the-number-of-virtual-sockets-and-the-number-
  of-cores-per-socket>`
- :ref:`Set vCPU reservation <set-vcpu-reservation>`


.. toctree::
   :maxdepth: 2
   :hidden:

   
   add-vcpu.rst
   remove-vcpu.rst
   adjust-the-number-of-virtual-sockets-and-the-number-
   of-cores-per-socket.rst
   set-vcpu-reservation.rst
   
