import streamlit as st
import main
st.title("Health Suggestions")
query = st.text_input("Enter your Query:")
received_data = main.question(query)
if st.button("Process"):
    # Call the Python file to process the query
    st.write("Processed Result:")
    st.write(received_data)
