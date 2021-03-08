.. _order-a-vm:


==========
Order a VM
==========

Order a VM when you want to deploy a new service or application.
As a best practice, install a new service or application on its own VM.
If you need to restart the VM, you impact all applications on that VM.

In a single VM order, you can order multiple VMs. You can order either an
exact copy of a VM, or you can make modifications to additional
VMs you order.

You can track the VM order fulfillment process. You receive a ticket
after the VM is available.

Before you begin, ensure that you are familiar with the following items:

* The compute destination of the VM (such as a vSphere cluster or
standalone ESXi server)
* The OS version you want (Windows and various Linux distributions)
* The network on which to connect the VM
* Port group names
* The domain in which to put a Windows VM
* Where to place the VM and the datastore names
* The sizes of the drives
* If you require managed backup on the VM
* The amount of vCPU and vRAM to allocate to the VM

**Important:** If you are unsure which VM parameters to choose, open a
ticket and request a consultation with us.

Complete the following steps to order a VM:

1. Log in to the Rackspace Technology Customer Portal.
2. In the **Products drop-down** menu, select
**VMware Server Virtualization.**
3. On the center panel, click **Order Virtual Machine.**
**The New Virtual Machine** order form appears.
4. In the **Deployment Destination** field, select the
vSphere Cluster or ESXi
host to which you want to add the VM.
5. In the **Image section**, select an operating system (OS) image you
want to use. Only the supported OSs on the destination are visible.
6.	In the **Configuration section**, complete the following steps:

      a.	Select a vCPU value. For more information about vCPU, \

see:ref:`understanding-vcpu`. You can change this value \
after the VM has been provisioned. \

      b.	Select a vRAM value. For more information about vRAM, see \

:ref:`understanding-vram`. \

      c.	Select a network. \

    The list contains networks that you have requested we create for you.
    We custom make these networks for your environment.

    **Note:** If you are unsure of which network to select, consult your
    internal team or contact your Rackspace Technology account team.

       d.	For Windows OSs, select an Active Directory Domain.

    **Note:** After you place the order, you cannot change your selection
    until we fulfill the order. If you are unsure of which domain
    to select, open a ticket and request a consultation.

    a.	In the **Storage** section, complete the following steps: \

        a.	Select the **Root Storage Device**. This is the VMFS datastore \
on which the first vDisk resides. For more information about \
root storage device options, \
see :ref:`understanding-storage`.
        b.	In the **Root Storage Size** field, enter the amount of storage \
to add to the first vDisk of your VM. \
        c.	In the **Root Mountpoint** field, enter the root mount point \
value. \
The **Root Mountpoint** can auto-allocate, depending on \
your selection. \
        d.	To add more vDisks, click **Add Storage**. \
And repeat these steps \
7.	In the **Security** section, under **Security Options**, select the \
desired option. \

We recommend that you select **Armor Anywhere** to protect yourself
from ransomware.

8.	In the **Identification** section, in the **Virtual Machine Name**
field, enter the virtual machine name.

The virtual machine name must be 6 to 70 characters long. If you
are creating a Windows-based VM, the hostname cannot be longer
than 8 characters.

**Note:** The system automatically adds a 6- or 7-digit Rackspace
device number prefix to the VM name.

9.	In the **Addon Services** section, in the Managed Backup field,
select your desired option for backups.

10.	If you agree with and accept our terms and conditions,
click **Confirm**.
11.	To order multiple VMs with the same configuration, complete
the following steps:
    a.	Select **Order multiple Virtual Machines with a \
        similar configuration and click **Next Step**.
    b.	Click **Add Virtual Machine Copies**.
    c.	Choose between **Exact Copies** or **Modified Copies**.
        If you select Modified copies, you can now make changes
        to these additional VMs.
    d.	Enter the desired number of copies in the **Quantity** field,
        then click **Copy Virtual Machine**.

12.	Accept the terms and then click **Order Virtual Machine** or
**Order Virtual Machines**. If the button is greyed out,
there is a problem with the current selection. For example, you might
have insufficient resources or a compatibility issue. Review your
options and try selecting another option or speak to the Virtualization
team for assistance.

Placing an order sends a ticket to your Rackspace VMware Support team
specialist. To track the progress of your order, see
:ref:`track-a-vm-order`.
