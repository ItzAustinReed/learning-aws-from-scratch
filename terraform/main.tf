terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "audit_logs" {
  bucket        = "my-aws-learning-audit-logs-2026"
  force_destroy = false

  tags = {
    Environment = "Dev"
    ManagedBy   = "Terraform"
    Project     = "AWS-Learning-Journal"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "audit_logs_encryption" {
  bucket = aws_s3_bucket.audit_logs.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
