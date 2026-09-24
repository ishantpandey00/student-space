import streamlit as st

st.set_page_config(page_title="Student Space", page_icon="🎓")

st.title("🎓 Student Space")
st.subheader("Your Study Space, Anywhere")

st.write("A website for students who do not have their own laptop.")

st.header("Our Features")

st.write("📁 Save academic files")
st.write("💻 Access your work from another computer")
st.write("🎤 Present your projects easily")

name = st.text_input("Enter your name")

if st.button("Get Started"):
    if name:
        st.success("Welcome " + name + " to Student Space! 🎉")
    else:
        st.warning("Please enter your name.")
