.. _change-the-association-between-a-vnic-a-port-group:



==================================================
Change the association between a vNIC a port group
==================================================



To connect a virtual network card to a different network segment, you can
request that we change the association between a vNIC and a port group.
Refer to :ref:`understanding-port-groups` for more information about port
groups.

You cannot change the association between a vNIC and port group yourself.
You must create a ticket and request that we change the association
for you.

To change the association between a vNIC and a port group, create a
Rackspace Technology ticket that includes the following information:

* The name of the VM and the vNIC you want to change.
* The name of the port group to which you want to associate the vNIC.
   
**Note:** When changing the association between a vNIC and a port group,
we must change IPs, which can result in downtime.



.. _change-vnic-type:




Change vNIC type
________________

Your VM might be compatible with multiple types of vNICs. By default,
your VM includes a VMXNET3 vNIC. If your software application requires,
you can change the vNIC to an E1000, E1000E, or VMXNET2 vNIC.

You cannot change the vNIC type yourself. To change the vNIC type,
create a Rackspace Technology ticket that includes the following
information:

* The name of the VM and the vNIC you want to change.
* The type of vNIC you want to use.
  
**Note:** When you make this request, plan for downtime.



.. _connect-or-disconnect-a-vnic:



Connect or disconnect a vNIC
____________________________

By default, a vNIC connects to the VM when the VM powers on.
When connected, the vNIC is ready to transmit data, just as
a network cable is ready to transmit data when plugged into
a physical machine.

You can request that we modify the following two vNIC
connection settings:

* **Current connection state:** By default, a vNIC is connected.
  A disconnected vNIC is offline and does not transmit data.
* **Connect at power on:** By default, a vNIC connects when the
  VM powers on. If the vNIC does not connect at power on, then
you must manually start the vNIC.

Though we rarely need to modify these, we might have to change these
settings to troubleshoot networking issues or if a VM is
involved in a security incident.

To request a vNIC connection or disconnection, create
a Rackspace Technology ticket that includes the following information:

* The name of the VM.
* The vNIC you want to change.
* The new setting (connect or disconnect)

