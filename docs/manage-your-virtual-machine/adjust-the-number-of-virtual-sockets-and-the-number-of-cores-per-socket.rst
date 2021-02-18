.. _adjust-the-number-of-virtual-sockets-and-the-number-of-cores-per-socket:

9.11.3

===============================================================
Adjust the number of sockets and the number of cores per socket
===============================================================

vCPU resource count is a product of two values:

* Number of virtual sockets
* Number of cores per socket
  
For example, if you have two virtual sockets and three cores per socket, 
then the total vCPU number is six.

By default, we build your VM with one core per socket, and 
the number of sockets matches your vCPU requirements.

To modify the number of cores for each socket, create a Rackspace Technology 
ticket and provide the following information:

* The VM name.
* The number of virtual sockets you want to allocate to the VM.
* The number of cores per socket you want to allocate to the VM.

**Note:** This change requires system downtime.






