# AWS Solutions Architect Associate (SAA-C03) Study Resources & Exam Guide

This document aggregates key learning notes, architecture decision trees, and preparation strategies for the **AWS Certified Solutions Architect – Associate (SAA-C03)** exam.

---

## 📌 Core Exam Focus Domains

To clear the SAA-C03 exam, you need a strong grasp of the **AWS Well-Architected Framework** across these primary domains:

* **Design Secure Architectures**: IAM policies, KMS encryption (SSE-S3, SSE-KMS), AWS Secrets Manager, and Security Groups / NACLs.
* **Design Resilient Architectures**: Multi-AZ deployments, Auto Scaling Groups, Application Load Balancers, and S3 Cross-Region Replication (CRR).
* **Design High-Performing Architectures**: Caching strategies (CloudFront, ElastiCache), DynamoDB DAX, and read replicas in Aurora / RDS.
* **Design Cost-Optimized Architectures**: S3 Lifecycle policies, Spot vs. On-Demand vs. Savings Plans, and Auto Scaling strategies.

---

## 📖 Recommended Community Write-ups & Experience Sharing

For a deep dive into real-world scenario analysis, preparation strategies, and exam day lessons, check out this detailed guide:

* [My Journey to AWS SAA-C03: Architecture Trade-offs, Preparation Tips, and Exam Day Lessons](https://telegra.ph/How-I-Passed-the-AWS-Solutions-Architect-Associate-SAA-C03-Exam-My-Proven-Study-Guide-08-16)

---

## 💡 Practical Test-Taking Strategies

1. **Identify the Constraint**: Always read the last sentence of the scenario first to see if it prioritizes *cost*, *performance*, *resilience*, or *minimal operational effort*.
2. **Eliminate Anti-Patterns**: Watch out for options that involve manual intervention, hardcoded credentials, or over-provisioned static instances.
3. **Pacing**: Aim for around 2 minutes per question to leave 10–15 minutes at the end to review flagged questions.

---

🔗 Official AWS Documentation & Certification Resources

* [AWS Certified Solutions Architect - Associate Official Page](https://aws.amazon.com/certification/certified-solutions-architect-associate/) - Exam guide, passing scores, and scheduling portal.
* [AWS Well-Architected Center](https://docs.aws.amazon.com/architecture-center/latest/well-architected/) - Architectural best practices and whitepapers.
* [AWS Documentation Portal](https://docs.aws.amazon.com/) - Official user guides and API references across all AWS services.
* [Official AWS GitHub Organization](https://github.com/awsdocs) - Open-source AWS documentation repositories and code samples.
