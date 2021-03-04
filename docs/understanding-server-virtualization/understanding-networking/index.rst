.. _understanding_networking:


========================
Understanding networking
========================

This section explains networking concepts that are important to understand
when you use Rackspace Server Virtualization.

The following diagram illustrates virtual and physical networking components
and their relationships to each other:

.. image:: Picture1.png


This section explains the following concepts:

- :ref:`Understanding vSwitches <understanding-vswitches>`
- :ref:`Understanding uplinks <understanding-uplinks>`
- :ref:`Understanding port groups <understanding-port-groups>`
- :ref:`Understanding vNICs <understanding-vnics>`



.. toctree::
   :maxdepth: 2
   :hidden:

    
   understanding-vswitches.rst
   understanding-uplinks.rst
   understanding-port-groups.rst
   understanding-vnics.rst







.. _understanding_vswitches:


Understanding vSwitches
-----------------------

Within ESXi, a vSwitch is a virtual switch, which is a logical construct
that provides a link between uplinks and port groups. A vSwitch can use
multiple uplinks and manage multiple port groups.

If a vSwitch uses two or more uplinks, a vNIC can only use one uplink at a
time. For example, if you have two 1000 Gbps uplinks connected to the
vSwitch and your VM connected to the port group connected to that vSwitch,
the maximum theoretical bandwidth for that VM is 1000 Gbps, rather than
2000 Gbps.

Your ESXi host usually has multiple vSwitches:

* A vSwitch that is connected to an external network (this is the primary
connection for your VMs).
* A vSwitch that is connected to a dedicated backup network.




.. _understanding_uplinks:


Understanding uplinks
---------------------

An uplink is the physical interface between the hypervisor and the
physical switch. An uplink is assigned to only one vSwitch. You can
refer to an uplink as *vmnicX*, with X being a sequential number of a
physical network ports on the hypervisor.



.. _understanding_port_groups:



Understanding port groups
-------------------------

A port group is a logical construct on the vSwitch to which vNICs can
connect. A port group typically has a name and a VLAN ID. You can see
the port group name shown as a network in the VMware Server Virtualization
section of the Rackspace Technology Customer Portal.

One port group can serve multiple vNICs.



.. _understanding_vnics:


Understanding vNICs
-------------------

A vNIC, or virtual network interface card, is a piece of the VM’s virtual
hardware. A vNIC provides an interface for the OS and connects to a
port group.

There are multiple types of vNICs, such as E1000 or E1000E. We recommend
using VMNXET3 for all VMs.

