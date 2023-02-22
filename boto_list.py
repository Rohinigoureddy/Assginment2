import boto3
s3_resource = boto3.resource('s3')
s3_resource.create_bucket(Bucket="aws-rohini")

for bucket in s3_resource.buckets.all():
    print(bucket.name)