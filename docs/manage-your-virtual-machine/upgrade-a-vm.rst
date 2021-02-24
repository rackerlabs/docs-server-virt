.. _upgrade-a-vm:


============
Upgrade a VM
============

This section describes how to upgrade the software that runs the VM. 

This section includes the following topics:

- :ref:`Upgrade VMware Tools <upgrade-vmware-tools>`
- :ref:`Upgrade virtual hardware compatibility version <upgrade-
  virtual-hardware-compatibility-version>`




.. toctree::
   :maxdepth: 2
   :hidden:

   self
   upgrade-vmware-tools.rst
   upgrade-virtual-hardware-compatibility-version.rst
   


To upgrade allocated virtual resources, refer to :ref:`manage-vDisk`,
:ref:`manage-vcpu`, and :ref:`manage-vram`.





.. _upgrade-vmware-tools:


Upgrade VMware Tools
____________________

VMware Tools`TM`:super: provides OS drivers for virtual hardware and enables
features such as vRAM ballooning and the graceful shutdown of the OS
in the Rackspace Technology Customer Portal. vRAM ballooning is a
memory reclamation technique that can negatively affect performance.

Occasionally, you need to upgrade VMware Tools. Upgrading VMware Tools
can provide additional functionality, update drivers, and address known
issues. A new VMware Tools version usually coincides with an ESXi release.
If you have configured your VM to automatically reboot during a
VMware Tools upgrade, ensure that you have scheduled the update for
hours outside your peak hours.

To upgrade VMware Tools, open a Rackspace Technology ticket and specify
the VM that contains the VMware tools that you want to upgrade. The host
determines the upgraded version.









.. _upgrade-virtual-hardware-compatibility-version:


Upgrade virtual hardware compatibility version
______________________________________________


The virtual hardware compatibility version is the VM version that
specifies the ESXi host versions with which the VM is compatible.
VMs with newer virtual hardware compatibility versions have increased
limits for the virtual hardware you can allocate.

New virtual hardware compatibility versions are available with
new ESXi releases.

To request an upgrade to the virtual hardware compatibility version,
open a Rackspace Technology ticket and specify the VM you want to upgrade.
We work with you to schedule the upgrade.
