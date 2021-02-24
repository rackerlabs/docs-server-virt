.. _manage-snapshots:



================
Manage snapshots
================

A VMware snapshot is a copy of the VM’s disk file (VMDK) at a given point
in time. Snapshots provide a changelog for the virtual disk, and you can
use them to restore a VM to a particular point in time when a failure or 
system error occurs.

Snapshot files that grow can affect VMs on the hypervisor.
For this reason, we recommend keeping a snapshot for no longer
than two days. After this time, you can delete the snapshot or revert to
the snapshot and original disks.

This section includes the following topics:
* Create a snapshot
* Delete a snapshot
* Revert to a snapshot




.. _create-a-snapshot:




Create a Snapshot
_________________


Create a snapshot when you want the option to roll back to it later.
Typically, you create snapshots before you upgrade an application or
patch an OS.

Before you take a snapshot, ensure that you have space on the datastore(s)
where this VM is stored. The size of the snapshot is equal to the
configured size of vRAM plus any increase due to changes. Changes to
the data in the VM contribute to the continuous growth of the snapshot.

1. Log in to the Rackspace Technology Customer Portal and click
   **Products > VMware Server Virtualization**.
2. Select the virtual machine you want to snapshot.
3. Scroll to the **Snapshots** section.
4. Click **Create Snapshot**.
5. Enter a description for your snapshot and click **Create Snapshot**.





.. _delete-a-snapshot:




Delete a Snapshot
_________________


When you delete a snapshot, all changes you made to the VM since you created
the snapshot are committed to the parent disk or snapshot. The VM stays
online during this process, but performance can be impacted.

The delete snapshot process can take between several minutes to several days,
depending on the snapshot’s age and size and the VM load. After you
delete the snapshot, you cannot restore it or revert to the
pre-snapshot VM.

Snapshot files that grow can affect VMs on the hypervisor. Do not keep a
snapshot for more than two days. After two days, delete the snapshot or
revert to the snapshot and original disks.

1. Log in to the Rackspace Technology Customer Portal and click
   **Products > VMware Server Virtualization**.
2. On the list of virtual machines, select the virtual machine for which
   you want to delete a snapshot.
   This action opens the virtual machine's details.
3. Scroll to the Snapshot section, click the gear icon next to the snapshot
   you want to delete, and click **Delete Snapshot**.
4. To confirm that you want to delete the snapshot,
   click **Delete Snapshot again**.




.. _revert-to-a-snapshot:




Revert to a Snapshot
____________________

When you revert a snapshot, the snapshot returns the VM to a previous state.
As a result, you lose any changes that you made after you created
the snapshot. This includes all data written to the VM during this time.

The VM reverts to the state it was when you took the snapshot. This means
that if you took the snapshot in a powered-off state, the VM reverts to a 
powered-off state. The VM also reverts to a powered-off state if
the snapshot does not include the memory. Otherwise, the VM continues to run.

**Note:** You cannot reverse a revert snapshot action.

1. Log in to the Rackspace Technology Customer Portal and click
   **Products > VMware Server Virtualization**.
2.	On the list of virtual machines, select the virtual machine for which
   you want to revert a snapshot.
This action opens the virtual machine's details.
3.	Scroll to the **Snapshot** section, click the gear icon next to the snapshot
   you want to revert, and click **Revert to Snapshot**.
4.	To confirm that you want to revert the snapshot, click **Revert**.















