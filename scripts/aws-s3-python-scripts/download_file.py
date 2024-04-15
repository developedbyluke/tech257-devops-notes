import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Variables
bucket_name = 'tech257-luke-test-boto3'
file_name = 'file.txt'

# Download the file
s3.download_file(bucket_name, file_name, file_name)
print(f"File '{file_name}' downloaded from bucket '{bucket_name}'.")
