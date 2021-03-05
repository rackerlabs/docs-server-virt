.. _understanding-remote-edition-initial-synchronization:



====================================================
Understanding remote edition initial synchronization
====================================================

After you define a VPG, the system updates the Zerto VRA in the
target site with information about the VPG. Then, it synchronizes
the data on the source VMs with the target VMs managed by the VRA
on the target site.

For the synchronization to work, ensure that the source VMs are
turned on. To synchronize across the sites, the Zerto VRA requires
an active input-output (IO) stack to have access to the VM data.
If the VM is not running, there is no IO stack to use to access
the protected data for replication to the target site recovery disks.

The synchronization process can take some time, depending on the size
of the source VMs, the amount of data in its volumes, and the bandwidth
between the sites. During this synchronization, you cannot perform
any replication task, such as failover operations.

**Note:** Initial synchronization can cause a spike in bandwidth usage
and might result in bandwidth overage charges.

After synchronization completes, the VRA on the target site includes
a complete copy of every VM in the VPG. At this time, the source VMs
in the VPG are fully protected, and the system sends the delta changes
on these VMs to the recovery site.



















