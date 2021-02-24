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

* Add vCPU
* Remove vCPU
* Adjust the number of virtual sockets and the number of cores per socket
* Set vCPU reservation


.. _add-vcpu:




Add vCPU
________

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

If you require assistance determining how many vCPUs to add, contact
your Rackspace Technology account team.

To add vCPU, refer to :ref:`resize-a-vm`.


.. _remove-vcpu:



Remove vCPU
___________

If your VM consistently underutilizes allocated vCPU resources, the VM
might be unnecessarily wasting physical CPU cycles on the hypervisor.
By removing vCPUs, you free up physical CPU resources for all VMs.
While removing vCPUs might sound counterintuitive, removing vCPUs could
actually improve the performance of all VMs running on the hypervisor,
including the VM in question.

If you require assistance determining how many vCPUs to remove,
create a Rackspace Technology ticket so we can run a report against your
environment and provide a recommendation.

To remove vCPU, refer to :ref:`resize-a-vm`.



.. _adjust-the-number-of-virtual-sockets-and-the-number-of-cores-per-socket:



Adjust the number of virtual sockets and the number of cores per socket
_______________________________________________________________________

vCPU resource count is a product of two values:

* Number of virtual sockets
* Number of cores per socket
  
For example, if you have two virtual sockets and three cores per socket,
then the total vCPU number is six.

By default, we build your VM with one core per socket, and
the number of sockets matches your vCPU requirements.

To modify the number of cores for each socket, create
a Rackspace Technology ticket and provide the following information:

* The VM name.
* The number of virtual sockets you want to allocate to the VM.
* The number of cores per socket you want to allocate to the VM.

**Note:** This change requires system downtime.


