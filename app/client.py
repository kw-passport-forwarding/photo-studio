import requests

BASE_URL = 'SD_INFERENCE_URL'


def post_sd_inference(file_name):
    response = requests.post(BASE_URL, json=dict(image=file_name))
    return response.json()['image']
