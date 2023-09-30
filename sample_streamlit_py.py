# -*- coding: utf-8 -*-
"""Sample_Streamlit.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BomiatbwOeO4Co7R7ta1uE4vxq0YbfhR
"""

import streamlit as st

# Title
st.title("Query Processor App")

# User Input
query = st.text_input("Enter your query:")

# Processing the Input
if st.button("Process"):
    # Call the Python file to process the query
    from process_query import process_query
    result = process_query(query)
    st.write("Processed Result:")
    st.write(result)
