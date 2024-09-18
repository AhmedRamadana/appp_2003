import streamlit as st

name = st.text_input("Enter your name")
button = st.button('show')

if button:
  st.write(f'Hello {name}')
