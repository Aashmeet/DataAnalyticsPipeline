""" Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. 
A copy of the License is located at: http://aws.amazon.com/apache2.0/
This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License. """

from __future__ import print_function

import boto3
from decimal import Decimal
import json
import urllib
from random import random
import base64
from s3transfer.manager import TransferManager
import datetime
import time
import os
import os.path
import sys
import tempfile
import botocore_deepinsight_beta

print('Loading function')

botocore_deepinsight_beta.setup_aws_data_path()

print('setting up boto3')

root = os.environ["LAMBDA_TASK_ROOT"]
sys.path.insert(0, root)
import json
import boto3
import urllib.parse
print('core path setup')

s3client = boto3.resource('s3')

print('initializing comprehend')
deepinsight = boto3.client(service_name='comprehend',
                           region_name='us-west-2', use_ssl=True)
print('done')

# --------------- Main Lambda Handler ------------------


def handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        object = s3client.Object(bucket, key)
        # create temp file with the review and download the review to it
        object.download_file('/tmp/sentiment.txt')

        file = open('/tmp/sentiment-out.csv', 'w')

        with open('/tmp/sentiment.txt') as f:
            for line in f:

                text = line
                ts = time.time()
                st = datetime.datetime.fromtimestamp(
                    ts).strftime('%Y-%m-%d %H:%M:%S')
                file.write(bucket + '/' + key + str(','))
                file.write(str(st) + str(','))

                sentiment_response = deepinsight.detect_sentiment(
                    Text=text, LanguageCode='en')
                print('sentiment detected')

                # Comprehend Sentiment Analysis call to set varibale and write to a csv row
                sentiment = sentiment_response["SentimentScore"]
                file.write(str(sentiment_response['Sentiment']) + str(','))
                file.write(str(sentiment['Positive']) + str(','))
                file.write(str(sentiment['Negative']) + str(','))
                file.write(str(sentiment['Neutral']) + str(','))
                file.write(str(sentiment['Mixed']) + str(',') + '\n')

        file.close()

        s3client.meta.client.upload_file('/tmp/sentiment-out.csv', Bucket=bucket, Key='sentiment/' + key + '.csv')

        return 'Sentiment Successfully Uploaded'
    except Exception as e:
        print(e)
        print(
            'Error: '.format(
                key, bucket))
        raise e
