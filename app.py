import streamlit as st

st.set_page_config(
    page_title="Student Space",
    page_icon="🎓"
)

st.title("🎓 Student Space")
st.subheader("Your Study Space, Anywhere")

st.write(
    "A website for students who do not have their own laptop."
)

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
    st.write("📁 Your files: 0")
    st.write("📚 Your projects: 0")
    st.write("🎤 Presentations: 0")

elif page == "Upload File":
    st.header("⬆️ Upload File")

    file = st.file_uploader(
        "Choose your academic file"
    )

    if file:
        st.success("File uploaded successfully! ✅")
        st.write("File name:", file.name)

elif page == "My Files":
    st.header("📁 My Files")
    st.info("Your saved files will appear here.")

elif page == "Presentation Mode":
    st.header("🎤 Presentation Mode")
    st.write(
        "Open your project here and present it easily."
    )
