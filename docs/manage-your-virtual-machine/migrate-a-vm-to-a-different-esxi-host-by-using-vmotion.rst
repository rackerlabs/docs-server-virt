.. _migrate-a-vm-to-a-different-esxi-host-by-using-vmotion:

9.13.1

======================================================
Migrate a VM to a different ESXi host by using vMotion
======================================================

You might need to migrate a VM to a different ESXi host. This migration 
process is called vMotion.

Request a vMotion when you want to:

* Migrate a VM to a new ESXi host.
* Migrate a VM from one vSphere cluster to another vSphere cluster.
  
The following diagram illustrates a VM migration process between two 
ESXi hosts in a cluster.

Image*
Picture1.png

**Important:**

* DRS might already be balancing VM placement within the cluster based on 
  host workload and DRS rules. If DRS automatically balances VM placement, 
  do not request a vMotion.
* If you vMotion a VM to another ESXi host when you have DRS in place, 
  you might reverse the vMotion migration or trigger a series of 
  subsequent vMotions.
* If you think that the DRS algorithm is not optimal, open a 
  Rackspace Technology ticket and request a consultation.

Subject to a variety of conditions, you can complete vMotion either offline 
or online. At a minimum, both source and destination hosts must have access 
to the shared datastore(s) where the VM’s vDisks are located. Open a ticket 
and ask us for a consultation so that we can advise you about what is 
possible based on your requirements.

The time required to execute a vMotion depends on the amount of vRAM 
allocated to VM and the overall resource allocation. An online vMotion 
might impact your environment

To request a vMotion, open a Rackspace Technology ticket and specify 
the following information:

* The VMs you want to migrate.
* The source and destination ESXi hosts or vSphere clusters.
* A timeframe for the migration.








