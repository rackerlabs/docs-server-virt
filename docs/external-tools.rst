.. _external_tools:

=====================================
Support for external monitoring tools
=====================================

External or third-party monitoring tools refer to monitoring tools that are
external to the cloud platform. Rackspace Technology current supports the
following tools:

- New Relic
- Datadog
- Prometheus AlertManager

Rackspace support of third-party tools is limited to the following:

1. Rackspace ingests only events from these sources and follows the
   documented monitoring runbooks.

2. Rackspace will not access these tools for any purpose. You are responsible
   for configuring and managing alerts.

3. If an equivalent monitor is available in the cloud vendor native tool,
   Rackspace recommends using these monitors, which enable Rackspace to
   better support the end-to-end workflow.

4. Rackspace provides recommended configuration settings and documentation
   to help you configure your monitoring tools to send events to the
   Rackspace ticketing system.

5. Rackspace works closely with you to ensure that the monitoring setup is
   working as expected, but you are ultimately responsible for the
   monitoring configuration.


.. _get_webhooks:

Getting the webhooks
--------------------

This section describes how to access webhooks for your third-party
monitoring tool.

.. note:: If you are using cloud vendor native tooling, such as AWS
   CloudWatch, Azure Monitoring, or GCP Cloud Monitoring, you don't need to
   do any additional setup. Rackspace automation configures cloud vendor
   native tools for all customers as per the service offering.

1. Log in to the
   `Rackspace Monitoring portal <https://manage.rackspace.com/monitoring>`_.

   The **Webhooks** page should display.

   .. image:: images/webhooks-page.png

2. In the **Account** section, select the account for which you want
   to add the monitoring tool.

   .. note:: Each account has its own set of webhooks, so be sure to configure
   your monitoring tool for the right account.

3. In the **Monitoring Service** section, select the tool that you want to add
   to your account.

4. In the **Severity** section, choose the appropriate priority level for
   incidents reported by your monitoring tool.

   .. image:: images/webhooks-example.png

   The webhook has the following format:

     - **Base URL** - https://watchman.api.manage.rackspace.com/
     - **Version** - API version. Currently v1 only
     - **Cloud Account** - The account type and number. For example,
       ``faws:accountNumber``, ``azure:subscriptionID``, or
       ``gcp:projectName``
     - **Webhook/service** - Service is the monitoring tool. For
       example, ``webhook/newrelic`` or ``webhook/datadob``
     - **Secret** - A unique value to the corresponding cloud account and
       severity combination
     - **Severity** - The supported severity levels are low, normal, high,
       urgent, and emergency.

5. Copy or save the webhook and use it to configure your monitoring tool.
   For more information about configuring tools, see :ref:`tool_configuration`.

If you have any issues, see :ref:`troubleshooting`.
