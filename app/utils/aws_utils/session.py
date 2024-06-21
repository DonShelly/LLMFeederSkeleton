import boto3
from flask import current_app


def boto3_session(region_name=None):
    """
    Return a boto3 session for the given region.

    If no region is given, the region set in the application config will be used.
    """

    if region_name is None:
        region_name = current_app.config.get("REGION", "us-east-1")

    if not current_app.config.get("SECRET_ACCESS_KEY") or not current_app.config.get(
        "ACCESS_KEY_ID"
    ):
        raise Exception("Missing AWS credentials")

    return boto3.Session(
        region_name=region_name,
        aws_secret_access_key=current_app.config.get("SECRET_ACCESS_KEY"),
        aws_access_key_id=current_app.config.get("ACCESS_KEY_ID"),
    )
