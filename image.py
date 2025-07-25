import cv2 as cv
import streamlit as st
import numpy as np
from PIL import Image
import base64

col1, col2, col3 = st.columns(3)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans&display=swap" rel="stylesheet">
<style>
    * {
        margin-left: 0;
        padding-left: 0;
    }
    
    html, body, [class*="css"] {
        
        font-family: "Pixelify Sans", sans-serif;
        color: "#453536";
        
    }
</style>
""", unsafe_allow_html=True)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def set_background_image(image_path):
    encoded_image = get_base64_image(image_path)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background_image("bg.jpg")

def to_grey(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def to_blur(img):
    blurred = cv.GaussianBlur(img, (65, 65), 0)
    return cv.cvtColor(blurred, cv.COLOR_BGR2RGB)

def detect_edges(img):
    return cv.Canny(img, 100, 200)

def detect_faces(img):
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

with col1:   
    st.markdown("""
        <h1 style="
            margin-left: 0;
            padding-left: 0;
            font-family: 'Pixelify Sans', sans-serif;
            color: #ff4b74"
            ">
            no ducking around, just quick edits
        </h1>
    """, unsafe_allow_html=True)

    
    upload_file = st.file_uploader("",  type =["png", "jpg", "jpeg"])
    if upload_file is not None:
        file_bytes = np.asarray(bytearray(upload_file.read()), dtype=np.uint8)
        img = cv.imdecode(file_bytes, 1)

        st.image(img, channels="BGR", use_container_width=True)
        st.markdown("""
            <link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans&display=swap" rel="stylesheet">
        """, unsafe_allow_html=True)

        if st.button('quack the colour away'):
            img_grey = to_grey(img)
            st.image(img_grey, use_container_width=True)


        if st.button('quack down the focus'):
            img_blur = to_blur(img)
            st.image(img_blur, use_container_width=True)

        if st.button('quack the edges'):
            img_edges = detect_edges(img)
            st.image(img_edges, use_container_width=True)