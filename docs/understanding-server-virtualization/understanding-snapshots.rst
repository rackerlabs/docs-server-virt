.. _understanding-snapshots:


=======================
Understanding snapshots
=======================

A snapshot represents a point-in-time state of the VM. Snapshots are
useful if you suspect a short-term rollback might be needed, such as
before starting a software upgrade on your VM.

When you take a VM snapshot, a delta file is created for each vDisk,
and all changes moving forward are written to the delta files. This
operation happens in the background and is not exposed to the Guest OS.

The delta files can grow rapidly and without your awareness. If the
delta files fill the datastore, your VM might pause, which can result
in unexpected downtime. Monitor the free space on your datastores and
delete all unneeded snapshots.


.. caution::
    As snapshot files grow, it can affect all virtual machines
    on the hypervisor. For this reason, we recommend keeping a snapshot for
    no longer than two days.
    
    Depending on the circumstances, you can delete snapshots within hours
    or days after being taken. When you delete the snapshot, the changes
    stored in the delta files are merged back onto the original vDisks.
    This operation can take a long time. You can also revert (roll back)
    to a snapshot, in which case the changes in the delta files are discarded.


.. note:: 
    Do not use a snapshot as a VM backup. VM replication is a
    better alternative for making and restoring backups.
