import streamlit as st
from PIL import Image
import os

# Define image folder path
images_path = "images"

# Display an image
st.header("Test Image Display")
test_image_path = os.path.join(images_path, "Zia.png")

if os.path.exists(test_image_path):
    st.image(test_image_path, caption="Test Image", use_column_width=True)
else:
    st.error(f"Image file not found: {test_image_path}")
