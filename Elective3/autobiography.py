import streamlit as st
from PIL import Image
import os

# Define the path to the 'images' folder
images_path = os.path.join(os.path.dirname(__file__), "images")

# Display an image
st.header("Test Image Display")
test_image_path = os.path.join(images_path, "Zia.png")

# Debugging output
st.write(f"Checking file: {test_image_path}")

if os.path.exists(test_image_path):
    st.image(test_image_path, caption="Test Image", use_column_width=True)
else:
    st.error(f"Image file not found: {test_image_path}")
