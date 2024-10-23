import streamlit as st

st.header("Basic Calculator!")

def square(num):
    return num * num

num = st.number_input("Insert a number")
st.write("The current number is ", num)

# How to call a function

# st st.button("Calculate Square", type="primary")
if st.button("Calculate Square"):
    result = square(num)

    st.subheader(result)