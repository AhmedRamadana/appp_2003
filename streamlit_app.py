import streamlit as st
import time

st.sidebar.title('calculate area')
area = None
st.header('calculate Area')

choose = st.selectbox("choose the shaape" , ['circle','rectangle'])

if choose=='circle':
  r = st.number_input('enter radius',min_value=1, max_value=100 )
  area = 3.14*r*r

elif choose=='rectangle':
  l = st.number_input('enter length',min_value=1, max_value=100)
  b = st.number_input('enter breadth',min_value=1, max_value=100)
  area = l*b

bt = st.button('calculate')

if bt:
  with st.spinner("loading...............")
  time.sleep(5)
  st.write(f'area={area} ')
