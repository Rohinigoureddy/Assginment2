import boto3
import cred

s3 = cred.resource('s3')
s3_resource = boto3.resource('s3')
s3_resource.create_bucket(Bucket="aws-rohini")

f = open('bucket_names.txt')
for bucket in s3_resource.buckets.all():
    f.write(bucket['Name'] + '\n')
