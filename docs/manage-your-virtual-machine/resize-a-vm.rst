.. _resize-a-vm:



===========
Resize a VM
===========

It is important to size VMs as close as possible to what you need because
you can easily add resources like CPU, memory, and disk, but removing
those resources requires a restart of the VM that results in downtime.

Rackspace recommends that you do not exceed the following resource
allocation ratios:

* 1:5 physical CPU to virtual CPU
* 1:1.25 physical RAM to virtual RAM
  
Before resizing a virtual machine, note that over-allocating resources can
negatively impact the performance of the VM and other VMs within your
environment.

**Caution:** Increasing vRAM consumes the same amount of datastore space which
in rare cases, can lead to downtime.

1. Log in to the Rackspace Technology Customer Portal and click
   **Products > VMware Server Virtualization**.
2. On the list of virtual machines, select the virtual machine you want
   to resize.
   This action opens the virtual machine's details.
3. **Click Actions > Resize VM**.
   This action automatically shuts down your VM, applies your change, and
   powers the VM back on.

4. Choose the new number of vCPUs and amount of vRAM.
5. Click **Resize Virtual Machine**.

When you click **Resize Virtual Machine**, the VM immediately powers off. 
The reboot process takes approximately five minutes.















