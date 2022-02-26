
import streamlit as st

@st.cache
def load_stuff():
    os.system('!curl https://raw.githubusercontent.com/b3n-j4m1n/salary-seeker/master/salary-seeker.sh > salary-seeker.sh')
    os.system('!chmod u+x *.sh')  

load_stuff()
st.markdown('hello world2')
