.. _datastore-overhead-requirements:


===============================
Datastore Overhead requirements
===============================

We require that your system have a certain percentage of each VMFS
datastore free at all times. The datastore overhead percentage depends
on the total capacity of each datastore.

Refer to the following minimum recommended datastore overhead values:

* For datastores with capacity up to 2048 GB, the overhead is 15%.
* For datastores with capacity between 2049 GB and 4096 GB,
  the overhead is 10%.
* For datastores with capacity greater than 4096 GB, the overhead is 7%.
* If VMs on the datastore use VM Replication or VM Recovery,
  the overhead is 15%.

**Note:** If the datastore is subject to multiple criteria listed above,
the criterion with the highest percentage takes priority.

This section includes the following topics:

- :ref:`Why is datastore overhead required? <why-is-datastore-overhead
  -required>`



.. toctree::
   :maxdepth: 2
   :hidden:

   
   why-is-datastore-overhead-required/index.rst
   
   