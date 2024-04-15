import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Variables
bucket_name = 'tech257-luke-test-boto3'

# Delete the bucket
s3.delete_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' deleted.")
