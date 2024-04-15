import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Variables
bucket_name = 'tech257-luke-test-boto3'
file_name = 'file.txt'

# Upload the file
s3.upload_file(file_name, bucket_name, file_name)
print(f"File '{file_name}' uploaded to bucket '{bucket_name}'.")
