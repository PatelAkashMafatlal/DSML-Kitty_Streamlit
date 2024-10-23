import streamlit as st

st.title("This is a Basic WebApp")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

agree = st.checkbox("I agree with suraaj")

if agree:
    st.write("Great!")

st.header("Radio Button")

genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"])

if genre == "Comedy":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

