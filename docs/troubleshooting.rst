.. _troubleshooting:

===============
Troubleshooting
===============

If you are having trouble setting up webhooks or configuring your monitoring
tools to connect to Watchman, perform the following troubleshooting steps:

- Confirm with your support team that the AWS account, Azure subscription, or
  GCP project has the AMR service offering. Third-party sources are
  supported only for AMR.
- In the third-party tool, ensure that the webhook is configured properly
  and using the right AWS account number, Azure subscription ID, or GCP
  project name in the URL.
- Isolate the issue by changing the source system to use an email address or
  alternative alerting system such as SMS or Pager Duty. If that works, the
  issue is with the webhook integration and the Rackspace engineering team
  can help you resolve the problem.
- Create a sample alert by using the samples provided in
  :ref:`tool_configuration`.

If you have another question or are having issues with the setup process,
open a ticket with your support team.
