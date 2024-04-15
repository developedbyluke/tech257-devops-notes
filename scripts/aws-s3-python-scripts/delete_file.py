import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Variables
bucket_name = 'tech257-luke-test-boto3'
file_name = 'file.txt'

# Delete the file
s3.delete_object(Bucket=bucket_name, Key=file_name)
print(f"File '{file_name}' deleted from bucket '{bucket_name}'.")
