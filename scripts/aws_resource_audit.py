import boto3
from botocore.exceptions import ClientError

# Python Boto3 Script: AWS Resource Audit for S3 & EC2

def audit_s3_buckets():
    s3 = boto3.client('s3')
    print("[*] Auditing S3 Buckets...")
    try:
        response = s3.list_buckets()
        for bucket in response.get('Buckets', []):
            print(f"  └── Bucket Name: {bucket['Name']}")
    except ClientError as e:
        print(f"  └── Access Denied or Error: {e}")

def audit_ec2_instances(region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    print(f"\n[*] Auditing EC2 Instances in Region: {region}...")
    try:
        response = ec2.describe_instances()
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_id = instance.get('InstanceId')
                state = instance['State']['Name']
                inst_type = instance.get('InstanceType')
                print(f"  └── ID: {instance_id} | Type: {inst_type} | State: {state}")
    except ClientError as e:
        print(f"  └── Error: {e}")

if __name__ == "__main__":
    print("=== AWS Baseline Infrastructure Audit ===")
    audit_s3_buckets()
    audit_ec2_instances()
