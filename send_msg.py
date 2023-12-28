import os
import time
import random

import boto3

aws_access_key_id = os.environ["AWS_KEY_ID"]
aws_secret_access_key = os.environ["AWS_KEY_SECRET"]
aws_region = "us-east-1"
queue_url = os.environ["QUEUE_URL"]

def main():
  start_time = time.time()
  duration_in_seconds = 5 * 60 * 60
  sqs_client = boto3.client("sqs", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

  while time.time() - start_time < duration_in_seconds:
    try:
      message_body = str(random.randrange(99999))

      response = sqs_client.send_message(
          QueueUrl=queue_url,
          MessageBody=message_body
      )
    except Exception as e:
      print(str(e))

    time.sleep(random.randint(1, 5))
    

if __name__ == "__main__":
    main()
