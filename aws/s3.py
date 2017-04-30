import boto3
s3 = boto3.resource('s3')

bucket_list = []

for bucket in s3.buckets.all():
    print bucket
    print(bucket.name)
    print(bucket.creation_date)
    bucket_list.append(bucket.name)
    print len(bucket.name)
    

    
