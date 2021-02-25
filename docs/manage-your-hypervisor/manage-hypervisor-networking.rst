.. _manage-hypervisor-networking:



============================
Manage hypervisor networking
============================


The amount and type of network capability you require on a hypervisor
can change over time based on your needs. To accommodate changes to
your applications, you can expand or remove vSwitches, port groups,
and uplinks. 

This section includes the following topics:

- :ref:`Add or remove a vSwitch <add-or-remove-a-vswitch>`
- :ref:`Manage port groups <manage-port-groups>`
- :ref:`Manage uplinks <manage-uplinks>`


.. toctree::
   :maxdepth: 2
   :hidden:

   
   add-or-remove-a-vswitch.rst
   manage-port-groups.rst
   manage-uplinks.rst









.. _add-or-remove-a-vswitch:



Add or remove a vSwitch
_______________________


A vSwitch, a virtual switch that provides a link between uplinks and port
groups, can use multiple uplinks and manage multiple port groups. Refer to
Understanding vSwitches[link] for more information about vSwitches.

To add or remove a vSwitch, open a Rackspace Technology ticket and
request a consultation.

**Note:** We cannot remove switches that we have pre-configured for you.



.. _manage-port-groups:




Manage port groups
___________________


A port group is a logical construct on the vSwitch to which vNICs can connect.
Refer to :ref:`understanding-port-groups` for more information about
port groups.

We manage port groups for you, including:

* Adding port groups
* Removing port groups
* Editing a VLAN ID
* Renaming a port group
  
If you require us to take any of the preceding actions, open a
Rackspace Technology ticket and indicate what action you want us to perform.

**Note:** Some port group tasks might require a maintenance window.



.. _manage-uplinks:




Manage uplinks
______________

An uplink is the physical interface between the hypervisor and the physical
switch. Refer to Understanding uplinks for more information about uplinks.

We manage your uplinks for you, including:

* Adding an uplink to a vSwitch
* Removing an uplink from a vSwitch
* Editing the priority of an uplink
* Moving a cable to a different port on the hypervisor
* Moving a cable to a different port on the physical switch, or to a
  different physical switch

If you require us to take any of the preceding actions, open a
Rackspace Technology ticket and indicate what action you want us to perform.

**Note:** Some uplink tasks might require a maintenance window.



