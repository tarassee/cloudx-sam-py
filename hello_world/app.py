import json
import os
import boto3

# import requests
sns_client = boto3.client('sns')


def lambda_handler(event, context):
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    result = process_queue_invocation(event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world 6",
            "invocation_source": result
            # "location": ip.text.replace("\n", "")
        }),
    }


def process_queue_invocation(event):
    # Check if Lambda was invoked from SQS
    if 'Records' in event:
        for record in event['Records']:
            msg_body = record['body']
            sns_message = json.dumps({"default": msg_body})
            send_to_sns(sns_message)
        return "Message sent to SNS from SQS invocation."
    else:
        # Assume invocation via API Gateway if 'Records' is not present
        sns_message = json.dumps({"default": "Called via API Gateway"})
        send_to_sns(sns_message)
        return "Message sent to SNS from API Gateway invocation."


def send_to_sns(sns_message):
    sns_topic_arn = os.getenv('AWS_SNS_TOPIC_ARN', 'default-topic-arn-if-none-specified')

    sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=sns_message,
        MessageStructure='json'
    )
