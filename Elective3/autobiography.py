import streamlit as st
from PIL import Image
import os

# Set page configuration
st.set_page_config(page_title="Christzia Marie Atay's Autobiography", page_icon="👩‍💻", layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: white;'>Christzia Marie Atay's Autobiography</h1>", unsafe_allow_html=True)

# Navigation
menu = ["Profile", "Experience", "Portfolio", "Contact"]
choice = st.sidebar.selectbox("Navigate", menu)

# Define image folder path
# Relative path to the images directory
images_path = "images"

# Profile Section
if choice == "Profile":
    st.header("About Me")
    st.write("---")
    st.write("""
    Taking ABM in Senior High School, currently pursuing a Bachelor of Science in Information Technology, expected to graduate in May 2025. 
    I passed the Third Year, where I cried my heart out, and now I am confident and manifesting in claiming the Diploma.
    """)

    st.write("### Personal Information")
    col1, col2 = st.columns([1, 2])
    with col1:
        # Display the picture from the images folder with specified width
        image_path = os.path.join(images_path, "Zia.png")
        if os.path.exists(image_path):
            with Image.open(image_path) as img:
                st.image(img, caption="Christzia Marie Atay", width=150)  # Adjust width as needed
        else:
            st.error(f"Image file not found: {image_path}")

    with col2:
        st.write(f"**Name:** Christzia Marie Atay")
        st.write(f"**Age:** 24 years old")
        st.write(f"**School:** Cebu Institute of Technology University")
        st.write(f"**Interests:** UI/UX, Frontend, and Quality Engineering")

    st.write("### My Skills")
    st.write("---")

    # Create columns for the skills section
    skill_col1, skill_col2, skill_col3 = st.columns(3)

    # Add skills to the respective columns
    with skill_col1:
        st.button("Python")
        st.button("Java")
        st.button("Figma")

    with skill_col2:
        st.button("C")
        st.button("MySQL")
        st.button("ClickUp")

    with skill_col3:
        st.button("React")
        st.button("OpenAI")
        st.button("Github")

# Experience Section
elif choice == "Experience":
    st.header("Experience")

    st.write("### ECW Part-time Encoder")
    st.write("**Work Setup:** Work from Home")
    st.write("**Dates:** March 23-25, 2022")
    st.write("**Responsibilities:**")
    st.write("- Encoding and managing data as per project requirements.")

    st.write("### Part-time Barangay Worker at Barangay San Nicolas Proper")
    st.write("**Dates:** January – June 30, 2018")
    st.write("**Responsibilities:**")
    st.write("- Writing reports of GAD Focal.")
    st.write("- Responsible for recording accurate details of constituents' personal background.")

# Portfolio Section
elif choice == "Portfolio":
    st.header("Portfolio")
    st.write("Here are some UI designs from my projects:")

    st.write("### UI for Capstone Project")
    # Path to the image for Capstone Project
    capstone_image_path = os.path.join(images_path, "Figma.png")
    if os.path.exists(capstone_image_path):
        with Image.open(capstone_image_path) as img:
            st.image(img, caption="UI for Capstone Project", use_column_width=True)
    else:
        st.error(f"Image file not found: {capstone_image_path}")

    st.write("### UI for System Integration Project")
    # Path to the image for System Integration Project
    system_integration_image_path = os.path.join(images_path, "Figma2.png")
    if os.path.exists(system_integration_image_path):
        with Image.open(system_integration_image_path) as img:
            st.image(img, caption="UI for System Integration Project", use_column_width=True)
    else:
        st.error(f"Image file not found: {system_integration_image_path}")

# Contact Section
elif choice == "Contact":
    st.header("Contact")
    
    st.write("Feel free to reach out to me through the following channels:")

    st.write("### LinkedIn")
    st.write("[Christzia Marie Atay's LinkedIn Profile](https://www.linkedin.com/in/christzia-marie-atay-388b80243/)")

    st.write("### Contact Number")
    st.write("+639 966 995 5095")

    st.write("### Email")
    st.write("christziamariea@gmail.com")
