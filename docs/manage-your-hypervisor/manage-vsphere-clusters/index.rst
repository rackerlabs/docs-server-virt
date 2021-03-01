.. _manage-vsphere-clusters:


=======================
Manage vSphere clusters
=======================

Members of a vSphere cluster, a collection of ESXi hypervisors,
pool their resources with a single VM drawing resources from one
hypervisor at a time. All cluster members have either identical,
or in some cases similar, configurations.

This section includes the following topics:

* View vSphere clusters
* Configure the distributed resource scheduler
* Configure high availability
* Distributed power management
* Add a resource pool


This chapter includes the following sections:

- :ref:`View vSphere clusters <view-vsphere-clusters>`
- :ref:`Configure the distributed resource scheduler
  <configure-the-distributed-resource-scheduler>`
- :ref:`Configure high availability <configure-high-availability>`
- :ref:`Distributed power management <distributed-power-management>`
- :ref:`Add a resource pool <add-a-resource-pool>`




.. toctree::
   :maxdepth: 2
   :hidden:

   
   view-vsphere-clusters.rst
   configure-the-distributed-resource-scheduler.rst
   configure-high-availability.rst
   distributed-power-management.rst
   add-a-resource-pool.rst
 


.. _view-vsphere-clusters:



View vSphere clusters
_____________________



You can use the Rackspace Technology Customer Portal to see the ESXi
hosts that form a part of a vSphere cluster. If you have multiple
vSphere clusters, you can see all of the clusters. Understanding the 
ESXi hosts that comprise a vSphere cluster is useful when you ask us
to make changes to multiple ESXi hosts. Instead of providing us with
he names of all hosts in the cluster, you can simply give us
the vSphere cluster name.

To see vSphere clusters and members:

1. Log in to the
   `Rackspace Technology Customer Portal<https://login.rackspace.com/>`_.
2. In the Products drop-down menu, select
   **VMware Server Virtualization**.
3. Click the Clusters tab.
4. Click the cluster name to see the details.

The number of cluster members (hypervisors) displays in
the **Details** section. Cluster members are listed by name
in **CPU allocation** and **Memory** sections.




.. _configure-the-distributed-resource-scheduler:




Configure the distributed resource scheduler
____________________________________________

Distributed Resource Scheduler (DRS) monitors the workload between
hypervisors and you can configure them to automatically move VMs
between ESXi hosts to address any imbalance.

For more information about DRS, refer to
:ref:`understanding-vmware-vsphere-clusters`.

To configure or modify DRS, open a Rackspace Technology ticket
and specify the DRS action you want us to take, including:

* Enable or disable DRS.
* Configure the DRS mode.
* Configure the DRS threshold.
* Configure DRS rules and groups.
* Configure VM overrides for DRS.




.. _configure-high-availability:


Configure high availability
___________________________



High availability (HA) is a feature that ensures system uptime to an
agreed-upon level.

VMware vSphere® High Availability monitors the ESXi host status, and
when a host fails, the vSphere HA feature automatically restarts
the VMs on remaining hosts.

To configure or modify high availability, open a Rackspace Technology
ticket and specify the HA action you want us to take, including:

* Enable or disable HA and include the cluster name.
* Set up VM overrides for HA
  **Note:** Provide us with the VM name and the HA override setting
  you want to apply to the VM.




.. _distributed-power-management:




Distributed power management
____________________________________________



Rackspace Server Virtualization does not support distributed
power management.



.. _add-a-resource-pool:




Add a resource pool
___________________


Use a resource pool to more granularly define how a VM uses CPU and RAM
resources. For example, we can define shares and limits for a
resource pool. VMs placed in a resource pool are then jointly subject to
these shares and limits.

Resource pools can sometimes produce undesired results. For example, if
you define a high-performance resource pool and then add many VMs to
that pool, the resources required by the VMs are higher than the proportion
of shares or limits available to the pool. Despite your intention to create
a high-performance pool, the VMs in that pool might perform worse than VMs
outside the pool.

If you want to set up a resource pool, open a Rackspace Technology ticket
and request a consultation.






