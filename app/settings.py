import os
from dotenv import load_dotenv

load_dotenv()


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
AWS_DEFAULT_BUCKET = os.getenv('AWS_DEFAULT_BUCKET')

SD_INFERENCE_URL = os.getenv('SD_INFERENCE_URL')
