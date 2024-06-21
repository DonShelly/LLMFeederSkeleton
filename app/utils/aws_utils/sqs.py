import json
import uuid

from botocore.exceptions import ClientError

from app import logger


def send_message(session, queue_url, message):
    """
    Send message to SQS queue
    :param session: boto3 session object
    :param queue_url: SQS queue URL
    :param message: message to send
    :return: bool
    """

    try:
        group_id = str(uuid.uuid4())
        session.client("sqs").send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message),
            MessageGroupId=group_id,
        )
    except ClientError as e:
        logger.error(f"Boto3 Client Error {str(e)}," f"Queue URL: {queue_url}")
        return False

    return True
