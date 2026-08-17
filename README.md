# AWS Learning Journal & Student Study Notes ☁️

Hey there! 👋 Welcome to my personal AWS learning hub. 

I’m currently a student diving deep into cloud architecture, hands-on lab experiments, and AWS certification prep. I created this repository to log my progress, summarize core AWS concepts, and document all the real-world trade-offs I discover while building projects on the AWS Free Tier.

---

## 💡 A Student's Perspective on Learning Cloud

Learning AWS as a student can feel overwhelming at first because there are so many services that sound similar. My goal here is to cut through the marketing jargon and focus on **practical understanding**—how services actually talk to each other and why we choose one over another.

### My Core Principles for Studying AWS:
* **Build First, Read Later**: Reading docs is great, but spinning up a VPC or deploying a serverless function in the console/CLI makes concepts stick 10x faster.
* **Cost Security is Priority #1**: Always set up AWS Budgets and Billing Alarms before launching anything! Forgetting a running NAT Gateway or EC2 instance is a painful rite of passage I'm actively trying to avoid. 😅
* **Think in Architecture**: Don't just memorize what a service does—understand *where* it fits into a multi-tier, resilient web architecture.

---

## 🎯 Key Topics & Service Notes

### 1. Compute & Serverless
* **EC2 vs. Lambda**: Choosing between traditional virtual machines (IaaS) for long-running processes vs. event-driven serverless functions (FaaS) for automated tasks.
* **Auto Scaling & Load Balancing**: Setting up Application Load Balancers (ALB) across multiple Availability Zones (AZs) for high availability.

### 2. Networking & VPC Essentials
* **VPC Subnet Design**: Public subnets (internet-facing) vs. Private subnets (isolated workloads).
* **NAT Gateways & Route Tables**: Understanding how private instances safely outbound to the internet for updates.

### 3. Storage & Databases
* **S3 Bucket Lifecycle Rules**: Transitioning data from S3 Standard to Infrequent Access (IA) and Glacier to optimize costs.
* **DynamoDB vs. RDS**: NoSQL single-digit millisecond key-value storage vs. managed relational SQL databases (PostgreSQL/MySQL).

---

## 📂 Repository Structure & Study Directory

### 📘 Certification Guides & Resources
* [`AWS-SAA-C03-Resources.md`](./AWS-SAA-C03-Resources.md) - Solutions Architect Associate exam domains, lab scenarios, and study guide.
* [`AWS_CLF_C02_Study_Guide_Notes.md`](./AWS_CLF_C02_Study_Guide_Notes.md) - Cloud Practitioner foundational concepts and service breakdowns.

### 📝 AWS Architecture Notes
* [`notes/AWS-Architecture-Notes.md`](./notes/AWS-Architecture-Notes.md) - Well-Architected Framework, VPC routing, and database design trade-offs.

### 🛠️ Automation & Python Scripts
* [`scripts/aws_resource_audit.py`](./scripts/aws_resource_audit.py) - Python Boto3 script for auditing S3 buckets and EC2 instance states.

---

## ⏱️ My Ongoing Learning Roadmap

- [x] Configure AWS Account, MFA, and Billing Alarms
- [x] Build a multi-AZ VPC from scratch with Public/Private subnets
- [ ] Deploy a containerized app using ECS / Fargate
- [ ] Complete scenario-based practice tests for SAA-C03

*Thanks for stopping by! Feel free to star ⭐️ this repo if you're also on your AWS learning journey.*
