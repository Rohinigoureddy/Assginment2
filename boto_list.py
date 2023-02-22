import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

with open('bucket_names.txt', 'w') as f:
   
    for bucket in response['Buckets']:
        f.write(bucket['Name'] + '\n')
