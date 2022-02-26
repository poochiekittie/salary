
import streamlit as st
import os

@st.cache
def load_stuff():
    os.system('!curl https://raw.githubusercontent.com/b3n-j4m1n/salary-seeker/master/salary-seeker.sh > salary-seeker.sh')
    os.system('!chmod u+x *.sh')  

load_stuff()
id = st.text_input('Input ID here: ')

if id:
    os.system('!./salary-seeker.sh ' + str(id) + ' > output.txt')  
    st.markdown(id)
    st.markdown('hello world3')
