# AWS SysOps Administrator Associate (SOA-C02 / SOA-C03) Operations Guide ⚙️💻

Focusing on system health, automated remediation, storage management, and cost optimization.

---

### 🛠️ Key Operational Business Scenarios

* **Automated Log Aggregation & Incident Remediation:**
  * *Scenario:* Detecting unauthorized IAM policy changes or EC2 SSH brute force attempts in near real-time.
  * *Implementation:* Configured CloudTrail logs streaming to CloudWatch Logs, filtering specific error patterns with Metric Filters. Set EventBridge rules to trigger AWS Systems Manager Automation Documents to automatically isolate compromised EC2 instances.
* **Storage Lifecycle & EBS Volume Optimization:**
  * *Scenario:* Reducing S3 storage costs and optimizing EBS performance for high-I/O database workloads.
  * *Implementation:* Configured S3 Lifecycle rules (Standard -> Intelligent-Tiering -> Glacier Flexible Retrieval). Automated the conversion of idle gp2 EBS volumes to gp3 using AWS Systems Manager State Manager scripts.

---

🔗 Official AWS SysOps Resources

* [AWS Systems Manager User Guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) - Automation, Patch Manager, Session Manager.
* [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) - Alarm management, logs insights, and custom metrics.

---

📚 Recommended External Exam Guides

* [AWS SysOps Administrator Associate (SOA-C02) Resource Guide](https://rentry.co/exam4pass-soa-c02)
* [AWS SysOps Administrator Associate (SOA-C03) Advanced Exam Notes](https://rentry.co/exam4pass-soa-c03)
