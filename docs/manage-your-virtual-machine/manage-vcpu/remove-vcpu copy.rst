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


