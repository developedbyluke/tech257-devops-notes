import boto3

s3 = boto3.client('s3', region_name='eu-west-1')
bucket_name = "tech257-luke-test-boto3"

try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1'
        }
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"Error creating bucket: {e}")
