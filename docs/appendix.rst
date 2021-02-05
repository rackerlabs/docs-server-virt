.. _appendix:

=====================
Appendix: Terminology
=====================

**AppDynamics (AppD)**
   An application performance monitoring (APM) tool that
   Rackspace Application Services uses.

**AppDynamics alert action**
   The action AppDynamics takes when an AppDynamics health rule violation
   occurs. An alert action can create tickets, notify your team, collect
   thread dumps, or execute remediation scripts.

**AppDynamics alert policy**
   Links AppDynamics health rules or other
   triggers to the desired AppDynamics alert action.

**AppDynamics health rule**
   Monitors that compare current application
   metrics, such as response time or error rates, to thresholds. Thresholds
   can be statically defined based on business needs, baselines automatically
   generated using past data, or a combination of the two.

**Application Performance Management (APM)**
   APM tools take raw data from your application and transform them into
   useful information about how smoothly your application runs and where
   potential bottlenecks might be. Rackspace uses either AppDynamics or New
   Relic as your APM tooling.

**Application Support Engineer (ASE)**
   ASEs are staffed 24x7 and have a broad set of knowledge across all the
   named apps that RAS Digital Experience supports.

**ARIC**
   A logic system that directs the actions of the Rackspace
   RBA automation tool.

**AWX**
   A central server and user interface used to run Ansible automation
   tasks within a customer environment. Rackspace ASEs use AWX to install
   and maintain RAS software and supported applications.

**Business transaction**
   A logical grouping of related URLs that allows your APM tool to
   consolidate metrics for multiple related pages, such as all
   checkout-related pages.

**Deployment**
   In the context of working with Rackspace Application Services, deployment
   is the process by which RAS pushes updated code or software components
   to the application. A deployment enables new features or fixes bugs.

**Jenkins**
   An automation tool used primarily for Oracle Web Commerce code deployments.

**Machine agent**
   A lightweight, standalone APM agent that reports operating system metrics
   such as CPU usage, network traffic, and so on.

**Named app**
   An application in which specific Rackspace engineers and architects
   specialize. Named apps engineers work regular US business hours but are
   available 24x7 to address production-down emergencies. The ASE team
   handles escalation to named apps engineers.

   The Linux named apps are ATG/Oracle Web Commerce, Adobe AEM, and SAP
   Hybris. The Windows named app is Sitecore.

**New Relic**
   A common APM tool used by Rackspace Application Services.

**New Relic alert condition**
   The New Relic implementation of a monitor. Alert policies compare current
   application metrics, such as response time or error rates, to
   thresholds. You can define alert thresholds based on business needs.

**New Relic alert policy**
   A group of one or more alert conditions linked to a New Relic
   Notification Channel.

**New Relic Notification Channel**
   New Relic uses a notification channel to create tickets or notify your
   team when an alert condition violation occurs.

**Runbook Automation (RBA)**
   Rackspace uses an RBA as the primary automation tool to create alert
   tickets and perform automated tasks in response to an alert.

**Synthetic monitor**
   Runs from remote pollers and mimics user actions on your website. Synthetic
   monitors test functionality similar to how your end users interact
   with the site.

**Thread dump**
   A saved snapshot of the execution stack for each JVM thread. Thread dumps
   enable Rackspace to see what each thread was doing at the time of the
   snapshot. You should take thread dumps when the issue or condition that
   you want to debug is active.

**Transaction snapshot**
   Provides detailed page load data, including a list of the slowest methods
   to execute and errors encountered during page load. Use transaction
   snapshots for troubleshooting.
