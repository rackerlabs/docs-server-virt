.. _understanding-test-operations:



=============================
Understanding test operations
=============================

We recommend that you periodically test the replication capabilities to ensure that the replication is working as expected. To begin planning a test, open a ticket with Rackspace Technology. During a test, the target VMs are powered on.

You have the following networking options for VMs that are tested on the secondary site. These options are pre-defined in the VPG settings:

*	**Use live production target site networks:** By default, live recovery networks are used. If the VMs are configured to use live networks, you might be able to access them, but it might also be required to temporarily suspend site-to-site VPN, depending on the configuration. This are the same networks that are used during a true failover. 

If you want to use one of the following options, open a Rackspace Technology ticket.

*	**Use dedicated testing networks with limited connectivity:** This option shares some elements of the live production target site networks and the bubble networks. Separate testing networks are set up that allow you to access the VMs, but the VMs have limited outside connectivity. You can work with us to define the connectivity rules.

*	**Use bubble network:** If the VMs are configured to use a bubble network, you won’t be able to access them. However, we verify via console if the OS has booted up successfully. A bubble network is an isolated network which isn’t connected to any other network.
During the test, the source site continues to run normally, and any changes you make on the target site are discarded at the end of the test. If instead you want to shut down the source VMs and run the VMs on the secondary site, consider planned failover instead.
