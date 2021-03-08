.. _understanding-vswitches:


=======================
Understanding vSwitches
=======================

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
connection for your VMs). \
* A vSwitch that is connected to a dedicated backup network.


