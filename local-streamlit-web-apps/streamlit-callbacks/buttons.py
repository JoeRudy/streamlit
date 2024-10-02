import streamlit as st

st.title("About Session...")

st.write(st.session_state)

if st.button("Button", key="my-button"):
    st.write("You clicked!")

st.write("Toggle is stateful")
if st.toggle("Toggle", key="my-toggle"):
    st.write("You toggled!")

st.write(st.session_state)
