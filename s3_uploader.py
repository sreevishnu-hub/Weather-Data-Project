# s3_uploader.py
import boto3
import json
from botocore.exceptions import BotoCoreError, ClientError

class S3Uploader:
    def __init__(self, bucket_name: str, region: str | None = None):
        self.bucket_name = bucket_name
        self.region = region

        self.s3_client = boto3.client(
            "s3",
            region_name=region,
        )

    def upload_json(self, data, key):
        try:
            json_bytes = json.dumps(data).encode("utf-8")

            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=json_bytes,
                ContentType="application/json"
            )

            return True

        except (BotoCoreError, ClientError) as e:
            print(f"Error uploading to S3: {e}")
            return False
