.. _understanding_vmware_vsphere_clusters:

2.3

=====================================
Understanding VMware vSphere clusters
=====================================

A VMware vSphere cluster is a collection of ESXi hypervisors that work
together. vSphere cluster members pool their resources with a single VM
that draws resources from one hypervisor at a time. All cluster members
have either identical, or, in some cases similar, configurations.

By default, and to further benefit from the clustered setup, Rackspace
Technology enables a Distributed Resource Scheduler and high availability.



.. _distributed_resource_scheduler:

2.3.1

Distributed resource scheduler
------------------------------

Distributed Resource Scheduler (DRS) monitors the workload between
hypervisors, and you can configure it to move VMs between ESXi hosts
and address any imbalance automatically. Refer to Move a VM between
two hosts or two datastores for more information about vMotion
migration.

DRS operates in the following three modes:

* **Fully automated (default, recommended):** When you power on a VM,
DRS moves running VMs and automatically selects the most suitable host.
* **Partially automated:** DRS automatically selects the most suitable
host when you power on a VM but only porvides recommendations to migrate
running VMs.
* **Manual:** DRS provides recommendations for the initial placement of
VMsand recommendations for running VMs but does not automatically migrate
running VMs.

Because the vSphere Cluster uses workload to determine the placement of the
VMs, the placement of VMs can appear random and not associated with your
business requirements. To control VM placement, you can ask us to configure
DRS rules.

Consider the following DRS rules categories:

*	**VM-VM Affinity:** Keep VMs together. Use this affinity setting if VMs
perform best when they run on the same host.
* **VM-VM Anti-affinity:** Keep VMs separate and prevent them from running
on the same host. If you have two web servers running on the same host, and
the host fails, both web servers go down.
**VM-Host rules:** Host rules apply to a group of VMs and a group of hosts.
Each group must include at least one member. Use the following options to
define a VM-Host rule:

    * A group of VMs should run on a group of hosts. This approach limits
    some VMs to run only on a set of hosts. You might want this option due
    to a specific hardware (for example, greater capability) advantage on
    those hosts. However, the rule is ignored when you place eligible hosts
    in maintenance mode and during an HA restart.
    *	A group of VMs must run on a group of hosts. VMs do not
    automatically migrate when you place all eligible hosts in maintenance
    mode. In addition, if no hosts in the defined group are available, HA
    might not restart the VMs.
    * A group of VMs should not run on a group of hosts. This rule is
    similar to the first VM-host rule, except that this rule defines the
    group of hosts that some VMs should avoid. For example, VMs are not
    placed in a group of hosts that are defined as part of the rule.
    * A group of VMs must not run on a group of hosts. The VMs avoid
    the specified hosts at all costs, even during an HA failover event.



.. _high_availability:

2.3.2

High availability
-----------------

VMware vSphere® HA monitors the ESXi host status, and when a host
fails, the vSphere HA feature automatically restarts the VMs on
remaining hosts.For the HA feature to function as intended, the
storage and networking must be consistent across all hosts in the
vSphere cluster.
