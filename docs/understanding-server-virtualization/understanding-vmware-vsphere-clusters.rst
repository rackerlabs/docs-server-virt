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