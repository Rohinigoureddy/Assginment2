import boto3

session = boto3.Session( 
         aws_access_key_id='IAM_User2', 
         aws_secret_access_key='Medhareddy@16')

s3 = session.resource('s3')

for bucket in s3.buckets.all():
  print(bucket.name)
  b=str(bucket.name)
  f= open("listtxt",'x')
f.write(b)