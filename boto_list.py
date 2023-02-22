import boto3

session = boto3.Session( 
         aws_access_key_id='AKIASH7DDKUJK3RDBDKJ', 
         aws_secret_access_key='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')

s3 = session.resource('s3')

f= open("list",'x')

for bucket in s3.buckets.all():
  print(bucket.name)
  b=str(bucket.name)
  
f.write(b)