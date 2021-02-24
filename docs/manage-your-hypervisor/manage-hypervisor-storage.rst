.. _manage-hypervisor-storage:



=========================
Manage hypervisor storage
=========================

The amount and type of storage you require on a hypervisor can change
over time based on your storage needs. To accommodate additional
applications and data, you can expand LUNs, local storage, and a
VMFS datastore.

While we cannot automatically shrink storage resources, we do
provide a workaround for situations where you need to reduce
storage capacity.

This section includes the following topics:

- :ref:`Expand LUNs <expand-luns>`
- :ref:`Shrink hypervisor storage <shrink-hypervisor-storage>`
- :ref:`Expand VMFS datastore <expand-vmfs-datastore>`
- :ref:`Manage host bus adapters <manage-host-bus-adapters>`


.. toctree::
   :maxdepth: 2
   :hidden:

   self
   expand-luns.rst
   shrink-hypervisor-storage.rst
   expand-vmfs-datastore.rst
   manage-host-bus-adapter.rst
  


.. _expand-luns:




Expand LUNs
___________


If you have requested that we expand your vDisk:ref:`understanding-storage`
or you have added VMs,we might recommend or require that you expand your
shared storage. Expanding a LUN :ref:`understanding-storage` comes with an
additional cost.

After expanding the LUN, we often expand the partition located on top of
the LUN. Most commonly, the partition is a VMFS datastore, or in the case
of an RDM LUN, a partition in the Guest OS.

**Important:** Before you agree to the increased cost, ensure that you
require the LUN expansion and not just a vDisk expansion
(although sometimes, you need both). If you are unsure of which type of
expansion you require, contact your Rackspace Technology account team.

To request that we expand a LUN, contact your Rackspace Technology account
team and provide the following information:

* Datastore name (if the LUN is formatted as a VMFS datastore) or partition
  letter (if the LUN is presented as an RDM).
* The gross amount or net usable amount of space you want to add.



.. _expand-vmfs-datastore:


Expand VMFS datastore
_____________________

When we expand a LUN :ref:`expand-luns`, we must also expand the VMFS
datastore. You can use the additional space to expand or add vDisks.

If your datastore was previously over-allocated before the expansion,
then the amount of useable new space might be less than you expect.
For more information about datastore overhead requirements,
refer to Datastore overhead requirements
:ref:`datastore-overhead-requirements`.

If you want us to expand a VMFS datastore, open a Rackspace Technology
ticket and provide the datastore name and the amount by which you want 
to expand it.





.. _manage-host-bus-adapters:



Manage host bus adapters
________________________

A host bus adapter (HBA) is hardware that you need for fiber channel
storage, such as shared SAN and dedicated SAN.

If you currently only have standalone hypervisors with local storage
and want to use SAN, we can install HBAs in each of your hypervisors.
Installing HBAs comes at an additional cost, and we install them during
a maintenance window.

To add an HBA, contact your Rackspace Technology account team and identify
the hypervisors for which you want us to add or remove HBAs. We usually
perform this work in a planned maintenance window.






