
import streamlit as st
import os

@st.cache
def load_stuff():
    os.system('!curl https://raw.githubusercontent.com/b3n-j4m1n/salary-seeker/master/salary-seeker.sh > salary-seeker.sh')
    os.system('!chmod u+x *.sh')  

load_stuff()
id = st.text_area('Input ID here: ')
st.markdown('hello world2')
