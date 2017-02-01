import boto3
import botocore
import json
import shutil
import glob2
import os
import time
from pywren import wrenhandler, wrenutil

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__)) 


class SQSInvoker(object):
    def __init__(self, region_name, sqs_queue_name):

        self.region_name = region_name
        self.sqs_queue_name = sqs_queue_name

        self.sqs = boto3.resource('sqs', region_name=region_name)

        self.queue = self.sqs.get_queue_by_name(QueueName=sqs_queue_name)
        

    def invoke(self, payload):
        """
        Invoke -- return information about this invocation
        """

        MessageBody = json.dumps(payload)
        response = queue.send_message(MessageBody=MessageBody)
        # fixme return something

    def config(self):
        """
        Return config dict
        """
        return {'sqs_queue_name_name' : self.sqs_queue_name, 
                'region_name' : self.region_name}

def sqs_run_local(region_name, sqs_queue_name, job_num=1):
    """
    Simple code to run jobs from SQS locally
    USE ONLY FOR DEBUG 
    """
    sqs = boto3.resource('sqs', region_name=region_name)
    
    queue = self.sqs.get_queue_by_name(QueueName=sqs_queue_name)


    for job_i in range(job_num):
        
        while True:
            response = queue.receive_messages(WaitTimeSeconds=10)

            if len(response) > 0:
                print "Dispatching"
                #pool.apply_async(
                process_message(response[0])
                
                wrenutil.local_handler([job], run_dir, 
                                       {'invoker' : 'SQSInvoker', 
                                        'job_i' : job_i})
                break
            else:
                print "no message, sleeping"
                time.sleep(4)