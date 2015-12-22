#!/usr/bin/env python
from boto.ec2 import EC2Connection
import json

csv_file = open('instances.csv','w+')
 
def process_instance_list(connection):
    map(build_instance_list,connection.get_all_instances())
 
def build_instance_list(reservation):
    map(write_instances,reservation.instances)
 
def write_instances(instance):
###### Nobody cares ###########################################################################################
#    if (instance.virtualizationType == 'hvm'):
#        platform = 'Windows'
#    else:
#        platform = 'Linux'
#    csv_file.write("%s,%s,%s,%s,%s,%s\n"%(instance.id,instance.public_dns_name,
#                                          instance.state,instance.placement,instance.architecture, platform))
#################################################################################################################

    # Beginning of alternate method if we choose to break out tags:

    # print 'test1\n'
    # for (tagname, tagvalue) in instance.tags.items():
    #   print tagname, tagvalue, '\n'
    # print 'test2\n'

    # csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,\"%s\"\n"%(instance.tags['Name'],instance.id,instance.public_dns_name,
    #                                       instance.state,instance.placement,instance.architecture,instance.instance_type,instance.launch_time,str(instance.tags)))
    csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,\"%s\"\n"%(instance.tags['Name'],instance.id,instance.public_dns_name,
                                          instance.state,instance.placement,instance.architecture,instance.instance_type,instance.launch_time,json.JSONEncoder().encode(instance.tags)))
    csv_file.flush()
 
if __name__=="__main__":
#    connection = EC2Connection(aws_access_key_id='AKIAJOCV3JTVUYTZSOWQ',aws_secret_access_key='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')
    connection = EC2Connection(aws_access_key_id='AKIAIB5FFTW3DXHAK4QA',aws_secret_access_key='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')

    process_instance_list(connection)
    csv_file.close()
