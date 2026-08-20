import boto3
from botocore.exceptions import ClientError

def check_s3_bucket_security():
    s3 = boto3.client('s3')
    print("[*] Starting S3 Bucket Security Audit...")
    
    try:
        buckets = s3.list_buckets().get('Buckets', [])
        for bucket in buckets:
            name = bucket['Name']
            print(f"\n[+] Auditing Bucket: {name}")
            
            # Check Public Access Block
            try:
                pab = s3.get_public_access_block(Bucket=name)
                print(f"    - Public Access Blocked: {pab['PublicAccessBlockConfiguration']['BlockPublicAcls']}")
            except ClientError:
                print("    - [!] WARNING: Public Access Block is NOT configured!")

            # Check Server-Side Encryption
            try:
                enc = s3.get_bucket_encryption(Bucket=name)
                rules = enc['ServerSideEncryptionConfiguration']['Rules']
                print(f"    - Default Encryption: Enabled ({rules[0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']})")
            except ClientError:
                print("    - [!] WARNING: Default Server-Side Encryption is NOT enabled!")

    except ClientError as e:
        print(f"[-] AWS API Error: {str(e)}")

if __name__ == '__main__':
    check_s3_bucket_security()
