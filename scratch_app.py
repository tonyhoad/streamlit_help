import streamlit as st
from time import time

# Function to build input form
def build_input():
    # print current session state
    st.write(f"build_input() executed with st.session_state at {time()} with session_state=")
    st.session_state

    # try to access disabled value
    if "disabled" not in st.session_state:
        st.session_state.disabled = False
    
    st.write(f"session_state immediately before text_input=")
    st.session_state

    st.text_input(label="Input text here",
        disabled=st.session_state.disabled)

    if st.button(label="Disable input", key="launch"):
        st.session_state.disabled=True
        st.session_state.clicked_at=time()

# Interface
build_input()

st.session_state