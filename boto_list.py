import boto3

ata_string = "This is a random string."

s3 = boto3.resource('s3')

object = s3.Object(
    bucket_name='Rohini-bucket', 
    key='output.txt'
)