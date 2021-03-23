.. _vmware-server-virtualization-architecture-options:



=================================================
VMware Server Virtualization architecture options
=================================================

When you subscribe to VMware Server Virtualization, for each layer
of the virtualization environment, you have a range of options from
which to choose.

For assistance in defining and configuring your Server Virtualization
environment request a consultation with your
Rackspace Technology Customer Success Manager.

During the pre-sales consultation, we help you determine your architecture
based on your requirements. Before the consultation, consider
the following questions:

* How many VMs do you need, and how many vRAM, vCPU, and storage resources does each VM require?
* What kind of performance and redundancy levels do you require for the CPU and RAM compute layer in all operational hosts in case one of the hosts in a cluster goes down, either unexpectedly or planned?
* What kind of storage performance and data redundancy levels do you require?
* What kind of network speed and network redundancy levels do you require?

The following diagram illustrates a common VMware Server Virtualization
environment, where:

* The ESXi hosts are installed on physical hardware and they host VMs. Multiple ESXi hosts form a cluster.
* Each ESXi host is connected to storage and networking. The VMs also use these resources.
* The VMs can be different sizes but do not span across ESXi hosts. VMs can vMotion between ESXi hosts. For more information about vMotion, refer to :ref:`move-a-vm-between-two-hosts-or-two-datastores`.

.. image:: server-virtualization-architecture-options1.png
