import boto3
from botocore.client import Config
s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))



bucket_list = [] 
objects = {}
object_list = []

sizes = []


for bucket in s3.buckets.all():
        bucket_list.append(bucket)
       
for bucket in bucket_list:
        for key in bucket.objects.all():
                #print key.key 
                sizes.append(key.size)
                objects.update({key.key:key.size})
                
for i in objects:
        print i, " ", (objects[i]/(1024*1024)),"MB"
        object_list.append(key.size)
        
print "There are ", len(objects), " objects in total"
print "The maximum value is ", max(object_list)
print "The total amount of data is ", (sum(object_list)/(1024*1024)), " Megabytes"

#for key in s3.buckets.all():
#        print "{name}\t{size}\t{modified}".format(
#                name = key.name,
#                #size = key.size,
#                modified = key.last_modified,
#                )
                