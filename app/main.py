import requests
import streamlit as st

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

    response_image = requests.get('https://images.khan.co.kr/article/2022/06/09/l_2022060902000459200088941.jpg')

    with output_content:
        st.subheader('Retouched photo')
        st.image(response_image.content, width=512)

