# AWS Certified Solutions Architect - Professional (SAP-C02) Enterprise Patterns 🏗️

Focusing on complex multi-tier enterprise migrations, disaster recovery architectures, and cloud financial management.

---

### 🏛️ Key Operational Business Scenarios

* **Hybrid Cloud Connectivity & Multi-Region Transit Gateway:**
  * *Scenario:* Connecting on-premises datacenters to 50+ VPCs across two AWS regions with redundant 10Gbps Direct Connect (DX) lines.
  * *Implementation:* Configured DX Gateway with IPsec VPN fallback (BGP routing), interconnected via AWS Transit Gateway peering, using AWS Route 53 Resolver rules for hybrid DNS resolution.
* **Multi-Region Active-Active Disaster Recovery (RPO < 1s, RTO < 1min):**
  * *Scenario:* Global e-commerce platform requiring seamless failover between `us-east-1` and `eu-west-1`.
  * *Implementation:* Deployed Amazon Aurora Global Database for storage-level cross-region replication, DynamoDB Global Tables, and Route 53 Application Recovery Controller (ARC) with latency-based routing and health checks.
* **Large-Scale On-Premises Migration:**
  * *Scenario:* Migrating 500+ legacy VMware VMs and SQL Server databases to AWS within a tight 6-month window.
  * *Implementation:* Utilized AWS Application Migration Service (MGN) for continuous block-level replication and AWS Database Migration Service (DMS) with Change Data Capture (CDC) for continuous database syncing.

---

🔗 Official AWS Enterprise Architecture Documentation

* [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) - The 6 pillars for enterprise cloud architecture evaluation.
* [AWS Prescriptive Guidance: Cloud Migration Framework](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/welcome.html) - Detailed migration strategies (6 Rs).
* [AWS Disaster Recovery Workloads Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) - Backup & Restore, Pilot Light, Warm Standby, Active-Active options.

---

📚 Recommended External Exam Guides

* [Passing AWS Solutions Architect Professional (SAP-C02) Essential Prep Notes](https://telegra.ph/Passing-AWS-SAP-C02-My-Essential-Prep-Notes-08-16)
