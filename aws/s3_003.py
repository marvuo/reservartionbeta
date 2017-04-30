import boto3
from botocore.client import Config
import sys

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))



class objekti(object):
    def __init__(self, name, size, bucket):
        self.name = name
        self.size = size
        self.bucket = bucket

dump = open("dump.txt",'w')
dump.truncate()


        
objektilista = [] 

for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        objektilista.append(objekti(key.key, key.size, bucket))

for i in objektilista:
    #print i.name,"\t", i.size,"\t", i.bucket
    a = (str(i.name) + "\t" +  str(i.size) + "\t" +str(i.bucket))
    dump.write(a)
    dump.write("\n")

def count_items():
    count = 0
    size = 0
    for i in objektilista:
       count +=1
       size += i.size
    print size
    return count
    
print "There was ", count_items()
dump.write("There was" + str(count_items()) + "objects in total")
    
dump.close()

#Let's store data to S3
data = open('dump.txt', 'rb')
s3.Bucket('lambdavuorinen').put_object(Key='data.txt', Body=data)
    
