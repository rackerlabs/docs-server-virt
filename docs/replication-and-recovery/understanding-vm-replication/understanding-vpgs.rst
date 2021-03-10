.. _understanding-vpgs:



==================
Understanding VPGs
==================

A Virtual Protected Group (VPG) enables you to protect, recover,
and test VMs together while maintaining write-order fidelity.
The Zerto VPG must include at least one VM. After Rackspace Technology
creates the default VPG, you can tell us how to group your source VMs
into VPGs. Consider the following examples:

**Group by customer**: If you host a set of VMs in VMware Server
Virtualization for each of your customers, you can create a VPG for
each customer. This configuration ensures that you maintain write-order
fidelity across all VMs.

**Group by workload or application**: If you host multiple workloads or
applications, you can group your VMs by each workload or application.
For example, for your production application, which comprises a database,
application, and web server, you can group VMs into a single VPG to ensure
write-order fidelity across all three tiers.

**Note:** All the VMs in a VPG must reside in the same VMware vCenter.

**VPG Properties**

For each Source VM, you need to provide Rackspace Technology the
following properties:

   * **VPG name**: The VPG name conforms to the following naming convention:
      
      *Account ID – Journal History Days – VMs*

      You can replace the VM value in the VPG name with a customer-defined name. Defining the appendix helps you identify the contents of the VPG.

      For example, if you group VMs by customers, use the customer name or ID. If you group VMs by application or workload, use a descriptor, such as *ProdCRM*, to represent your Production CRM application.

   * **Journal history days**: The target length of time you can roll back VMs within a VPG upon recovery.

      By default, each VM has a value of seven days. Setting the Zerto Journal History to seven days provides the ability to specify a recovery point-in-time within the last seven days.

      For example, if you accidentally decommission the wrong VMs and need to recover the VMs, but it takes you five days to identify the mistake, you can select the checkpoint before the decommission because you have a seven-day journal full of checkpoints.

      **Note:** The actual journal history size depends on the available storage. Configuring longer journal history requires the storage capacity to keep all changes for the desired period. The configured target might not be met, and journal checkpoints that have not met the desired journal history target might be automatically deleted if there is insufficient space.

   * **Boot order:** The order in which the VMs contained within a VPG boot upon recovery. VMs boot in ascending order.

      For example, suppose the VPG includes a database, application tier, and web server tier, and the database must be available before the application tier or web server. In that case, you can set the database boot order to 1, application tier to 2, and web server to 3.

   * Failover IP range: 

      * **Private:** By default, and subject to availability, when a VM fails over to the target site, we set the private IPs to match the source IPs. You can customize this to a different IP.
      * **Public:** When a VM fails over to the target site, its public IP address is automatically changed. Public Blocks are assigned out of the target site location.


