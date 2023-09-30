import streamlit as st
st.title("Health Suggestions")
query = st.text_input("Enter your name:")
received_data = None
def receive_data(data):
    global received_data
    received_data = data
if st.button("Process"):
    # Call the Python file to process the query
    st.write("Processed Result:")
    st.write(received_data)
