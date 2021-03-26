.. _expand-luns:



===========
Expand LUNs
===========


If you have requested that we expand your vDisk :ref:`understanding-storage`
or you have added VMs,we might recommend or require that you expand your
shared storage. Expanding a LUN :ref:`understanding-storage` comes with an
additional cost.

After expanding the LUN, we often expand the partition located on top of
the LUN. Most commonly, the partition is a VMFS datastore, or in the case
of an RDM LUN, a partition in the Guest OS.

.. important::
  Before you agree to the increased cost, ensure that you
  require the LUN expansion and not just a vDisk expansion
  (although sometimes, you need both). If you are unsure of which type of
  expansion you require, contact your Rackspace Technology account team.

To request that we expand a LUN, contact your Rackspace Technology account
team and provide the following information:

* Datastore name (if the LUN is formatted as a VMFS datastore) or partition
  letter (if the LUN is presented as an RDM).
* The gross amount or net usable amount of space you want to add.


