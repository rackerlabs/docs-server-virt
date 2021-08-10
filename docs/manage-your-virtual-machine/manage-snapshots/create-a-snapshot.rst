.. _create-a-snapshot:


=================
Create a Snapshot
=================


Create a snapshot when you want the option to roll back to it later.
Typically, you create snapshots before you upgrade an application or
patch an OS.

Before you take a snapshot, ensure that you have space on the datastore(s)
where this VM is stored. The size of the snapshot is equal to the
configured size of vRAM plus any increase due to changes. Changes to
the data in the VM contribute to the continuous growth of the snapshot.

1. Log in to the Rackspace Technology Customer Portal and click **Products > VMware Server Virtualization**.
2. Select the virtual machine you want to snapshot.
3. Scroll to the **Snapshots** section.
4. Click **Create Snapshot**.
5. Enter a description for your snapshot and click **Create Snapshot**.

