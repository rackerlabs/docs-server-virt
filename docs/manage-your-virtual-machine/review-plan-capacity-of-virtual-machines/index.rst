.. _review-plan-capacity-of-virtual-machines:



========================================
Review plan capacity of virtual machines
========================================

We provide performance metrics and usage statistics for VMs and ESXi hosts.
The statistics provides insight into how your environment is performing,
which can help you optimize your environment and plan for expansion.

This section includes the following topics:

- :ref:`What is capacity planning? <what-is-capacity-planning>`
- :ref:`Review performance metrics of VM <review-performance-metrics-of-vm>`
- :ref:`View VM configurations <view-vm-configurations>`


.. toctree::
   :maxdepth: 2
   :hidden:

   
   what-is-capacity-planning.rst
   review-performance-metrics-of-vm.rst
   view-vm-configurations.rst



.. _what-is-capacity-planning:



What is capacity planning?
__________________________


As your business grows, so do your VMs. Although the resources that VMs
consume are finite, you can take some steps to anticipate need and plan
for future growth. Capacity planning is the process of reviewing the
resource usage of VMs and estimating their growth so that you can
proactively expand your physical resources before you need them.
Without capacity planning, you might not be able to build new VMs
or expand your existing VMs, and your environment might slow over time.

You are responsible for estimating your future growth needs, for example,
telling us how many new VMs you need and how many resources you expect
each of them to consume.

We can provide the details about current usage. Many metrics are already
available on the Rackspace Technology Customer Portal.

After you have existing data and future growth estimates, contact your
Rackspace Technology account team.




.. _review-performance-metrics-of-vm:




Review performance metrics of VM
________________________________



The Rackspace Technology Customer Portal provides a number of useful
vCenter metrics that help you understand how your VMs are used.
Available metrics include but are not limited to CPU, network, RAM, and
storage.

Complete the following steps to view metrics in the
Rackspace Technology Customer Portal .


1. Log in to the `Rackspace Technology Customer Portal
   <https://login.rackspace.com/>`_
2. In the **Products** drop-down menu, select
   **VMware Server Virtualization**.
3. Navigate to a VM, an ESXi hypervisor, or a vSphere cluster for which you
   want to see the metrics.
4. Scroll to the **Performance** section. In this section, you can
   perform the following actions:
   * Select the metric you want to see.
   * Change the time range you want to see.
   * Observe the graph shown based on your selections.
   * Export data to **.csv** format for further analysis.



.. _view-vm-configurations:


View VM configurations
______________________



The Rackspace Technology Customer Portal enables you to view the
following VM configuration details:

* The amount of vRAM :ref:`understanding-vram` and vCPU
* :ref:`understanding-vcpu`that is allocated to the VM. \
* The ESXi host :ref:`understanding-hypervisors` on which the VM is running.
* The list of vDisks :ref:`understanding-storage` and where the vDisks are
  located on the VM.
* The network(s) :ref:`understanding-networking` the VM is connected to.
* In-process vCenter :ref:`understanding-vmware-vcenter` tasks.

To view the configuration of a VM, complete the following steps:

1. Log in to the
   `Rackspace Technology Customer Portal <https://login.rackspace.com/>`_
2. In the **Products** drop-down menu, select
   **VMware Server Virtualization**.
3. Select the VM for which you want to see the configuration. \

A page displays the details of the VM.









