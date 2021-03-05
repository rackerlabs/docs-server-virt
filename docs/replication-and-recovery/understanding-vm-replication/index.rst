.. _understanding-vm-replication:


============================
Understanding VM replication
============================

VM Replication Enhanced Edition, powered by the Zerto® IT
Resilience Platform™, delivers a fully managed always-on experience.
With Recovery Point Objectives (RPOs) and Recovery Time Objectives (RTOs)
measured in seconds and minutes, VM replication provides near-continuous
storage-agnostic data replication enabling the recovery of VMs from
business-impacting events such as ransomware, hardware failures,
or natural disasters. VM Replication offers both local and
remote replication.

This section includes the following topics:

- :ref:`Understanding VM replication key features <understanding-vm-replication-key-features>`
- :ref:`Understanding VM replication architecture <understanding-vm-replication-architecture>`
- :ref:`Understanding how VM replication protection works <understanding-how-vm-replication-protection-works>`
- :ref:`Understanding Remote Edition Initial Synchronization <understanding-remote-edition-initial-synchronization>`
- :ref:`Understanding Remote Edition Continuous Replication <understanding-remote-edition-continuous-replication>`
- :ref:`Understanding VPGs <understanding-vpgs>`
- :ref:`Understanding test operations <understanding-test-operations>`
- :ref:`Understanding failover operations <understanding-failover-operations>`
- :ref:`Understanding VM replication roles and responsibilities <understanding-vm-replication-roles-and-responsibilities>`





.. toctree::
   :maxdepth: 2
   :hidden:

    
   
   understanding-vm-replication-key-features.rst
   understanding-vm-replication-architecture.rst
   understanding-how-vm-replication-protection-works.rst
   understanding-remote-edition-initial-synchronization.rst
   understanding-remote-edition-continuous-replication.rst
   understanding-vpgs.rst
   understanding-test-operations.rst
   understanding-failover-operations.rst
   understanding-vm-replication-roles-and-responsibilities.rst

  
**Note:** You cannot configure VMs that have one of the following
characteristics for a source VM:

* Active Directory VMs (We support and recommend Active Directory
  native replication.)
* VMs with raw device mappings (RDMs).
* Multi-write disk mode.
* Oracle clusters.
* RHEL clusters.


