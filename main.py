import streamlit as st
from PIL import Image


def display(img):
    # convert the pillow image to grayscale
    gray_img = img.convert("L")

    # display the grayscale image on the webpage
    st.subheader("this your gray scaled image")
    st.image(gray_img)


def check(image):
    try:
        if image:
            pic = Image.open(image)
            display(pic)
    except:
        st.write("please choose a valid image to continue")


st.header("Color to grayscale convertor")

with st.expander("Start the camera"):
    # starting the camera
    new_image = st.camera_input("Camera")
    check(new_image)

with st.expander("Upload an image"):
    # open de file browser
    new_image = st.file_uploader("Browser")
    check(new_image)

with st.expander("About this WebApp"):
    # open the about page
    content = """
    This a simple webapp that allow the users to transform images into gray scaled images. the user has the possibility 
    to take directly a picture throw the camera or upload an image throw the WebApp using the files browser.\n
    CAMERA MODE:
    The user must click first on "Start the camera" to expend the menu. then, he must just give permission to the WebApp
    so that it can access to the connected camera. Then click on "Take Photo" to have a magnific gray scaled photo. 
    After the button clicked, bellow the camera field will appear the
    taken picture in a gray scaled mode.\n
    UPLOAD MODE:
    The user must click first on "Upload an image" to expand the menu. then click on the "Browse files" button to open 
    a file browser window and choose an image. After the image selected and submitted, bellow the field will appear the
    selected image in a gray scaled mode.
    """
    st.write(content)
