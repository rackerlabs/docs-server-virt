.. _remove-vcpu:


===========
Remove vCPU
===========

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


