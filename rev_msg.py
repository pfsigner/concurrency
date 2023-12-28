import os

import boto3

aws_access_key_id = os.environ["AWS_KEY_ID"]
aws_secret_access_key = os.environ["AWS_KEY_SECRET"]
aws_region = "us-east-1"
queue_url = os.environ["QUEUE_URL"]

main():
  sqs_client = boto3.client("sqs", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

  while True:
    try:
      response = sqs_client.receive_message(
        QueueUrl=queue_url,
        AttributeNames=["All"],
        MaxNumberOfMessages=10,
        MessageAttributeNames=["All"],
        WaitTimeSeconds=20
      )

      if "Messages" in response:
        message = response["Messages"][0]
        print(f"Received message: {message["Body"]}")

        sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message["ReceiptHandle"]
        )
    except Exception as e:
      print(str(e))
    

if __name__ == "__main__":
    main()
