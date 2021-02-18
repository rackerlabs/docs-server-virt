.. _understanding-how-vm-replication-protection-works:

11.1.3

=================================================
Understanding how VM replication protection works
=================================================

With Zerto's hypervisor-based continuous data replication, Zerto 
copies every write to the VM and sends it, asynchronously, to 
the target site. At the same time, the source site continues 
to process the write.

On the target site, Zerto writes the write to a journal managed by 
the Zerto Virtual Replication Appliance (VRA). Each protected 
VM has a unique journal. Every few seconds, the system writes 
a checkpoint to each journal. These checkpoints ensure write-order 
fidelity and crash-consistency to each checkpoint. During recovery, 
one of the crash-consistent checkpoints is selected and recovered 
to this point.

The Zerto VRA manages the journals for every source VM to be 
recovered to the hypervisor hosting that VRA. It also manages 
the images of the protected volumes for these target VMs. 
During a failover, you can specify that you want to recover 
the source VMs in the VPG by using the last checkpoint. 
Alternatively, you can specify an earlier checkpoint, 
in which case the system synchronizes the recovery of 
the mirror images under the VRA to the chosen checkpoint. 
Thus, you can recover the environment to the point before 
any corruption and ignore later corrupted journal writes. 
The cause of the corruption, such as a crash in the source site 
or a ransomware attack, does not affect the recovery process.
