.. _move-a-vm-to-a-datastore-by-using-storage-vMotion:



=================================================
Move a VM to a datastore by using storage vMotion
=================================================


You might need to vMotion a VM’s vDisk(s) to a different datastore.
This migration process is called storage *vMotion*.

Request a storage vMotion when you want to balance the free space on
the datastore.

Subject to a variety of conditions, you can complete vMotion either
offline or online. At a minimum, both source and destination datastores
must be accessible from the ESXi host where the VM is running.
Open a ticket and ask us for a consultation so that we can advise you
about what is possible based on your requirements.

The time required to execute a vMotion depends on the size of the vDisks
connected to the VM and storage performance. An online vMotion might impact
your environment.

The following diagram illustrates a vDisk migration from one LUN or
datastore to another LUN or datastore.

.. image:: Picture5.png

To request a storage vMotion, open a Rackspace Technology ticket and
specify the following information:

* The VMs or the vDisks you want to migrate
* The source and destination datastores
* A timeframe for the migration

