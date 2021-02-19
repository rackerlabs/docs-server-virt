.. _understanding_storage:


=====================
Understanding storage
=====================

This section explains the following storage concepts that are important to
understand when you use VMware Server Virtualization.

* **Logical Unit Number (LUN):** A LUN identifies a storage device. In the 
context of VMware, a LUN provides a foundation for a VMware filesystem
(VMFS) datastore, or you can use it as an **Error!**
**Reference source not found.**

* **Datastore:** A datastore is a volume formatted with a VMFS. You can
create a VMFS datastore on top of a LUN or on a local RAID array.
A VMFS datastore contains log files or files that comprise VMs.

* **vDisk:** A vDisk is a virtual disk. A Guest OS in the VM uses a vDisk
in the same way it would use a physical disk but represents the vDisk as
a **.vmdk** file on a VMFS datastore.

The following graphic illustrates VMs that are connected to vDisks of
different sizes. The vDisks reside on a VMFS datastore with some of the
datastore space reserved. The datastore is formatted on top of a LUN.

.. image:: Picture2.png

* **Raw Device Mapping:** Raw Device Mapping (RDM) is a type of storage 
configuration where a LUN is mounted to the VM directly, bypassing the
datastore layer. Bypassing the datastore layer means that the Guest OS 
in the VM can issue Small Computer System Interface (SCSI) commands
directly to the LUN. This configuration is most commonly used with
Microsoft clustering. However, using RDMs means you cannot use features
such as snapshots or VM-level backups. Other operations, such as
storage vMotion, might also become more complex.

The following image illustrates two clustered VMs using their own vDisks
and sharing two raw device LUNs. The pointer files, which reside on the
VMFS Datastores alongside the vDisks, act as a proxy between the LUNs and
the VMs.

.. image:: Picture3.png 






