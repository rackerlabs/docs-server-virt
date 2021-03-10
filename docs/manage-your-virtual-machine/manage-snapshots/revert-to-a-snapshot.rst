.. _revert-to-a-snapshot:


====================
Revert to a snapshot
====================


When you revert a snapshot, the snapshot returns the VM to a previous state.
As a result, you lose any changes that you made after you created
the snapshot. This includes all data written to the VM during this time.

The VM reverts to the state it was when you took the snapshot. This means
that if you took the snapshot in a powered-off state, the VM reverts to a
powered-off state. The VM also reverts to a powered-off state if
the snapshot does not include the memory. Otherwise, the VM continues
to run.

**Note:** You cannot reverse a revert snapshot action.

1. Log in to the Rackspace Technology Customer Portal and click **Products > VMware Server Virtualization**.
2. On the list of virtual machines, select the virtual machine for which you want to revert a snapshot.
   This action opens the virtual machine's details.
3. Scroll to the **Snapshot** section, click the gear icon next to the snapshot you want to revert, and click **Revert to Snapshot**.
4. To confirm that you want to revert the snapshot, click **Revert**.
