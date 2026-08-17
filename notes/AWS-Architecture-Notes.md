# AWS Cloud Architecture & Well-Architected Framework Notes

Designing scalable and resilient systems on AWS requires adhering to the **AWS Well-Architected Framework** while making calculated trade-offs between cost, performance, and operational complexity.

> **Key Takeaway:** Decoupling application components via asynchronous messaging (SQS/SNS) ensures fault tolerance and prevents cascading failure across distributed workloads.

## 1. The AWS Well-Architected Framework (6 Pillars)

* **Operational Excellence:** Automating deployments, responding to events, and managing everyday operations via infrastructure as code.
* **Security:** Protecting data in transit and at rest using IAM policies, KMS encryption, and network isolation (VPC).
* **Reliability:** Executing automated recovery from failures and designing multi-AZ/multi-region architectures.
* **Performance Efficiency:** Selecting optimized instance types and leveraging caching (CloudFront, ElastiCache).
* **Cost Optimization:** Rightsizing compute, utilizing Savings Plans / Reserved Instances, and tiering S3 storage.
* **Sustainability:** Minimizing energy consumption by optimizing cloud resource utilization.

## 2. VPC Networking & Traffic Flow

* **Public vs. Private Subnets:** Public subnets route traffic through an **Internet Gateway (IGW)**. Private subnets route outbound traffic securely via a **NAT Gateway** located in a public subnet.
* **Security Groups vs. Network ACLs:** Security Groups are stateful firewalls at the ENI/instance level. Network ACLs (NACLs) are stateless rules operating at the subnet boundary.

## 3. Storage & Database Selection Criteria

* **S3 Storage Classes:** Standard (frequent access) -> Intelligent-Tiering (auto-cost optimization) -> Standard-IA -> Glacier Flexible / Deep Archive (long-term retrieval).
* **RDS vs. DynamoDB:** RDS provides relational OLTP engines with Multi-AZ automated failover. DynamoDB delivers single-digit millisecond NoSQL key-value performance at scale.
