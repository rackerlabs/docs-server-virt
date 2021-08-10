.. _understanding-failover-operations:



=================================
Understanding failover operations
=================================



There are two types of failover operations:

* **Planned failover.** Use a planned failover when you want to move to your secondary site. Regulatory purpose might require this kind of failover, or you might need to prove that your business can operate normally when running on a secondary site. To plan this, open a ticket with Rackspace Technology.

* **Unplanned failover.** Use an unplanned failover when an unexpected and adverse event occurs, and you need to fail over immediately. Call Rackspace Technology for help with executing an unplanned failover.

During a failover, source VMs are shut down (if they are not already down).
To move back to the original site, you must first do a reverse protection.

To improve the RTO during recovery, you can start working even before
the target VM volumes on the target Site have been fully synchronized.
The system analyses every request and response returned from the
Target VM directly or from the journal if the information in the
journal is more current. This process continues until the recovery
site virtual environment is fully synchronized, up to the chosen
checkpoint when the integrity of the protected site was assured.

