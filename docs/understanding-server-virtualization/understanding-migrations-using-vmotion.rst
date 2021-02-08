.. _understanding_migrations_using_vmotion:

2.10

======================================
Understanding migrations using vmotion
======================================

There are two forms of VM migration to consider when working with 
Server Virtualization. The first form of migration is an initial 
migration that occurs when you become a Rackspace Technology customer 
and migrate an existing workload to Server Virtualization. 
See Migrate a workload to VMware Server Virtualization [link to Migrate
an existing workload to VMWare Server Virtualization] for 
more information about migrating a workload from another environment 
to Server Virtualization. 

**Note:** Don’t use vMotion to migrate external workloads to 
Server Virtualization or migrate a VM from RPC-V to Server Virtualization.

The other form of migration refers to the methods by which VMs are migrated 
from one host or datastore to another host or datastore within the 
VMware Server Virtualization environment. This form of migration happens 
either on a daily basis, often without your awareness as a result of 
automated action, or because you requested it.

The following forms of migration are available depending on what you 
need to move:

* **vMotion:** vMotion is the technology that we use to migrate a VM from 
one ESXi host to another ESXi host. Depending on the circumstances, 
the migration can occur either offline or online. DRS uses vMotion 
automatically to balance the load between ESXi hosts.

* **Storage vMotion:** Storage vMotion migrates a VM from one VMFS 
datastore to another. The target datastore must have sufficient space. 
Storage vMotion migration can take a long time to complete, so your 
system might experience performance degradation during the 
migration operation.

* **vMotion without Shared Storage:** vMotion without Shared Storage 
combines vMotion and storage vMotion. vMotion without Shared Storage is 
most commonly used for migration between two standalone hypervisors.




