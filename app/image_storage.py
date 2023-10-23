from datetime import datetime

import boto3

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_BUCKET


class Boto3Client:
    def __init__(self):
        self.client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

    def upload(self, file, file_name):
        extension = file_name.split('.')[-1]
        self.client.upload_fileobj(
            file,
            AWS_DEFAULT_BUCKET,
            f'input/{file_name}-{datetime.now().isoformat()}.{extension}'
        )


boto3Client = Boto3Client()
