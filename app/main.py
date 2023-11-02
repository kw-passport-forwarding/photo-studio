import streamlit as st

from client import post_sd_inference
from image_storage import boto3Client

# page setting
st.set_page_config(
    page_title='passport forwarding',
    layout="wide"
)

# title
st.title('KW passport forwarding')

# layout
empty1, input_content, arrow_content, output_content, empty2 = st.columns([0.1, 1.0, 0.2, 1.0, 0.1])

# content
img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])


if img_file is not None:
    with input_content:
        st.subheader('Your photo')
        st.image(img_file, width=512)
        saved_file_name = boto3Client.upload(img_file, img_file.name)

    with output_content:
        st.subheader('Retouched photo')

        inferenced_file_name = post_sd_inference(saved_file_name)
        response_image = boto3Client.download(inferenced_file_name)
        st.image(response_image, width=512)

