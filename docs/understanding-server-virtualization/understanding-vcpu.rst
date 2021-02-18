.. _understanding-vcpu:



==================
Understanding vCPU
==================

A VM includes one or more virtual central processing units (vCPU).
By allocating vCPUs to VMs, you can share physical CPUs on the hypervisor
with the VMs.

Over-allocating CPU can negatively impact system performance. You should
only allocate as many vCPU resources as your VM needs. If you allocate more
cores than you need, you waste CPU cycles that could be used by your
other VMs.

____________________________