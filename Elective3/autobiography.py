import streamlit as st  # type: ignore
from PIL import Image  # type: ignore

# Set page configuration
st.set_page_config(page_title="Christzia Marie Atay's Autobiography", page_icon="👩‍💻", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio("Go to", ["🏠About Me", "🎨Portfolio", "📩Contact Me"])
st.sidebar.write("---")
st.sidebar.write("© 2024 by Christzia Marie A. Atay. All rights reserved.")

# --- MAIN / ABOUT ME ---
if selected_tab == "🏠About Me":
    st.title("About Me")

    # "Professional Summary" section
    st.subheader("📄 Professional Summary")
    st.write("""
        To gain practical experience in the IT field by applying foundational knowledge in software development, testing,
        and design to real-world projects. I aim to enhance my skills in programming, 
        problem-solving, and collaboration within a professional setting.
        Eager to contribute effectively to team goals while learning industry best practices in a hands-on environment.
    """)
    st.write("---")

    # Personal Data and Image Section
    left_column, right_column = st.columns([4, 3])
    with left_column:
        st.subheader("📋 Personal Data")
        st.write("""
            **Age**: 25  
            **Date of Birth**: November 29, 1999  
            **Gender**: Female  
            **Religion**: Roman Catholic  
            **Marital Status**: Single  
        """)
    with right_column:
        st.image("images/Zia.png", width=300)

    # Core Qualifications
    st.write("---")
    st.subheader("💻 Core Qualifications")
    st.write("""
        - Figma, Canva  
        - Python, Java, HTML, CSS  
        - Firebase, MySQL, Postman, Trello, ClickUp, GitHub  
        - Android Studio, Visual Studio Code, ReactJS  
        - PowerPoint, MS Word, Excel  
        - Strong Work Ethic  
        - Time Management  
        - Critical Thinking  
    """)

    # Certifications
    st.write("---")
    st.subheader("📜 Certifications")
    st.write("""
        - Huawei - Information Representation and Data Organization  
        - Tech Intern to Tech Expert: Crafting Resumes and Mastering Interviews  
        - Huawei - HCIA-Storage  
        - Data Analytic Introduction to Machine Learning  
        - Employment Readiness Seminar  
        - Software Testing Tutorial  
        - Introduction to Java  
    """)

    # Educational Background
    st.write("---")
    st.subheader("🎓 Educational Background")
    st.write("""
        **College Diploma**  
        Cebu Institute of Technology-University, Cebu City  
        Bachelor of Science in Information Technology  
        S.Y. 2021 – Present  

        **Senior High School Diploma**  
        Don Carlos A. Gothong Memorial National High School  
        S.Y. 2021 – 2021  
    """)

    # References
    st.write("---")
    st.subheader("📞 References")
    st.write("""
        - **Dr. Leah V. Barbaso**: Capstone and Research Adviser at Cebu Institute of Technology – University  
          Email: leah.basbaco@cit.edu.ph  

        - **Dr. Patrick L. Bacalso**: CCS OJT Coordinator at Cebu Institute of Technology - University  
          Email: patrick.bacalso@cit.edu.ph  
    """)

# --- PORTFOLIO ---
elif selected_tab == "🎨Portfolio":
    st.title("🎨 Project Portfolio")
    section = st.selectbox("Select a Section", ["Capstone and Research", "System Integration and Architecture", "Application Development and Emerging Technologies"])

    if section == "Capstone and Research":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("images/Capstone/C1.png", use_column_width=True)
            st.image("images/Capstone/C4.png", use_column_width=True)
        with col2:
            st.image("images/Capstone/C2.png", use_column_width=True)
            st.image("images/Capstone/C5.png", use_column_width=True)
        with col3:
            st.image("images/Capstone/C3.png", use_column_width=True)
            st.image("images/Capstone/C6.png", use_column_width=True)

    elif section == "System Integration and Architecture":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("images/SI/SI1.png", use_column_width=True)
            st.image("images/SI/SI4.png", use_column_width=True)
        with col2:
            st.image("images/SI/SI2.png", use_column_width=True)
            st.image("images/SI/SI5.png", use_column_width=True)
        with col3:
            st.image("images/SI/SI3.png", use_column_width=True)
            st.image("images/SI/SI6.png", use_column_width=True)

    elif section == "Application Development and Emerging Technologies":
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image("images/AppDev/A1.png", use_column_width=True)
        with col2:
            st.image("images/AppDev/A2.png", use_column_width=True)
        with col3:
            st.image("images/AppDev/A3.png", use_column_width=True)
        with col4:
            st.image("images/AppDev/A4.png", use_column_width=True)

# --- CONTACT ME ---
elif selected_tab == "📩Contact Me":
    st.title("📩 Contact Me")
    left_column, right_column = st.columns([1.8, 1.2])

    with left_column:
        st.subheader("Contact Form")
        contact_form = """
        <form action="https://formsubmit.co/christziamariea@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here..." required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        st.markdown("""
            <style>
            form {
                display: flex;
                flex-direction: column;
            }
            input, textarea, button {
                margin: 5px 0;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
            </style>
        """, unsafe_allow_html=True)

    with right_column:
        st.subheader("Get in Touch")
        st.write("""
            Feel free to reach out to me through any of the platforms below:  

            - **Email**: christziamariea@gmail.com  
            - **Phone**: +63 966 995 5095  
        """)

# --- END ---
