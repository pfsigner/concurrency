import os
import time

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
      response = sqs_client.receive_message(
        QueueUrl=queue_url,
        AttributeNames=["All"],
        MaxNumberOfMessages=10,
        MessageAttributeNames=["All"],
        WaitTimeSeconds=20
      )

      if "Messages" in response:
        for message in response["Messages"]:
          print(f"Received message: {message['Body']}")

          sqs_client.delete_message(
              QueueUrl=queue_url,
              ReceiptHandle=message["ReceiptHandle"]
          )
    except Exception as e:
      print(str(e))
    

if __name__ == "__main__":
    main()
