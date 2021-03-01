.. _connect-or-disconnect-a-vnic:


============================
Connect or disconnect a vNIC
============================

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

