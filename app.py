import streamlit as st

st.set_page_config(
    page_title="Student Space",
    page_icon="🎓"
)

st.title("🎓 Student Space")
st.subheader("Your Study Space, Anywhere")

st.write("A website for students who do not have their own laptop.")

if "files" not in st.session_state:
    st.session_state.files = []

if "presentation_file" not in st.session_state:
    st.session_state.presentation_file = None

st.sidebar.title("Menu")

page = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Dashboard", "Upload File", "My Files", "Presentation Mode"]
)

if page == "Home":
    st.header("🏠 Home")
    st.write("Welcome to Student Space!")
    st.write("Access your academic work from anywhere.")

elif page == "Dashboard":
    st.header("📊 Student Dashboard")
    st.write("Welcome to your dashboard.")
    st.write("📁 Your files:", len(st.session_state.files))
    st.write("📚 Your projects: 0")
    st.write("🎤 Presentations: 0")

elif page == "Upload File":
    st.header("⬆️ Upload File")

    file = st.file_uploader(
        "Choose your academic file",
        type=["pdf", "pptx", "docx", "txt"]
    )

    if file:
        st.session_state.presentation_file = file

        if file.name not in st.session_state.files:
            st.session_state.files.append(file.name)

        st.success("File uploaded successfully! ✅")
        st.write("File name:", file.name)

elif page == "My Files":
    st.header("📁 My Files")

    if len(st.session_state.files) == 0:
        st.info("No files uploaded yet.")
    else:
        for file_name in st.session_state.files:
            st.write("📄", file_name)

elif page == "Presentation Mode":
    st.header("🎤 Presentation Mode")

    if st.session_state.presentation_file is not None:

        file = st.session_state.presentation_file

        st.success("Your presentation is ready! 🎉")
        st.write("File:", file.name)

        if file.name.endswith(".pdf"):
            st.pdf(file)

        else:
            st.info(
                "Your file is uploaded. "
                "Download it and open it in PowerPoint to present."
            )

    else:
        st.info("Please upload a file first.")
    
