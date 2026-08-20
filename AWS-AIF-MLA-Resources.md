# AWS Certified AI Practitioner (AIF-C01) & ML Engineer (MLA-C01) Prep Notes 🤖🧠

Covering enterprise Generative AI implementation, Amazon Bedrock integration, and end-to-end MLOps pipeline management.

---

### 🔬 Key Operational Business Scenarios

* **Enterprise RAG System with Amazon Bedrock Guardrails:**
  * *Scenario:* Building an internal enterprise search engine using LLMs while preventing sensitive PII leakage and hallucination.
  * *Implementation:* Implemented Retrieval-Augmented Generation (RAG) using Amazon Bedrock Knowledge Bases paired with Amazon OpenSearch Serverless vector index. Configured Bedrock Guardrails for PII redaction and toxic prompt filtering.
* **Automated MLOps Pipeline with SageMaker:**
  * *Scenario:* Training, evaluating, and deploying custom fraud detection models with continuous retraining based on data drift.
  * *Implementation:* Utilized Amazon SageMaker Pipelines for automated workflow orchestration, SageMaker Feature Store for feature reusability, Model Registry for version control, and SageMaker Clarify for model explainability/bias detection.

---

🔗 Official AWS AI/ML Documentation

* [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) - Foundation Models, Guardrails, Knowledge Bases, and Agents.
* [Amazon SageMaker MLOps Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/mlops.html) - Model governance, pipelines, and continuous deployment workflows.
* [AWS Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-data-privacy-and-governance-on-aws/) - Security controls for GenAI workloads.

---

📚 Recommended External Exam Guides

* [AWS Certified AI Practitioner (AIF-C01) Resource Compilation](https://rentry.co/exam4pass-aws-ai-guide)
