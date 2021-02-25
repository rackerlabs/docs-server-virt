.. _manage-vnics:


============
Manage vNCIs
============

VMs typically include the following two virtual network interface
cards:ref:`understanding-vnics`.

* **Public interface:** The public interface vNIC is the primary connection.
* **Dedicated backup network interface:** If you subscribe to
  the Rackspace Technology managed backup service, the dedicated backup
  network vNIC is used for file backup traffic.

While you cannot manage a vNIC yourself, we provide a list of information
for the following tasks that you should include in your ticket so that we
can expedite your request.

This section includes the following topics:

- :ref:`Add a vNIC <add-a-vnic>`
- :ref:`Remove a vNIC <remove-a-vnic>`
- :ref:`Change the association between a vNIC a port group <change
  -the-association-between-a-vnic-a-port-group>`
- :ref:`Change vNIC type <change-vnic-type>`
- :ref:`Connect or disconnect a vNIC <connect-or-disconnect-a-vnic>`


.. toctree::
   :maxdepth: 2
   :hidden:

   
   add-a-vnic.rst
   remove-a-vnic.rst
   change-the-association-between-a-vnic-a-port-group.rst
   change-vnic-type.rst
   connect-or-disconnect-a-vnic.rst
   





.. _add-a-vnic:



Add a vNIC
__________

If required by your software application, you can add a vNIC to a VM.

You cannot add a vNIC yourself. You must create a ticket and request that
we add the vNIC for you.

To add a vNIC, create a Rackspace Technology ticket that includes the
following information:

* The name of the VM.
* The port group name to which the vNIC should connect.
  
Unless you specify otherwise, we configure the vNIC as a VMXNET3 interface.
For more information about vNIC types, refer to :ref:`understanding-vnics`.



.. _remove-a-vnic:



Remove a vNIC
_____________

When you no longer need a vNIC that you have added (for example, if you
have uninstalled the application that requires the vNIC), you can request
that we remove it.

**Note:** Do not request that we remove either of the default vNICs.
If either of the default vNICs is removed, you lose access to your VM,
and any backups might stop working.

To remove a vNIC, create a Rackspace Technology ticket that includes
the following information:

* The VM to which the vNIC connects.
* The name of the vNIC you want removed.




.. _change-the-association-between-a-vnic-a-port-group:




Change the association between a vNIC a port group
__________________________________________________



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

