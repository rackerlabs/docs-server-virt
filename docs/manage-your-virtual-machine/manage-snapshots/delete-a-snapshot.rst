.. _delete-a-snapshot:


=================
Delete a snapshot
=================


When you delete a snapshot, all changes you made to the VM since you
created the snapshot are committed to the parent disk or snapshot.
The VM stays online during this process, but performance can be impacted.

The delete snapshot process can take between several minutes
to several days, depending on the snapshot’s age and size and the
VM load. After you delete the snapshot, you cannot restore it or revert
to the pre-snapshot VM.

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
4. To confirm that you want to delete the snapshot, click
   **Delete Snapshot again**.
