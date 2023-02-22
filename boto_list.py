import boto3

session = boto3.Session( aws_access_key_id='Rohini14', aws_secret_access_key='Medha@16')

s3 = session.resource('s3')

my_bucket = s3.Bucket('Rohini')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)