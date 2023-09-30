# -*- coding: utf-8 -*-
"""Sample_Chatbot_Huggingface.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fsFXrrc4R0pnXWfA9cIetd63DjG3tUuY
"""

!pip install transformers

!pip install streamlit

from transformers import pipeline
import pandas as pd
import streamlit as st

# Load the pre-trained model for question answering
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# Define a function to interact with the chatbot
def chatbot(question):
    # Provide a context or passage where the answer can be found
    with open("/content/Data.txt", "r", encoding="utf-8") as file:
        context = file.read()
    # Use the question-answering model to find the answer
    answer = qa_pipeline(question=question, context=context)

    return answer

# # Interact with the chatbot
# def prints(questions):
#     response = chatbot(questions)
#     # print(f"Question: {question}")
#     print(f"Answer: {response['answer']}")
#     print(f"Confidence: {response['score']:.4f}")
#     print()

# Interact with the chatbot
def prints(questions):
    response = chatbot(questions)
    # print(f"Question: {question}")
    print(f"Answer: {response['answer']}")
    print(f"Confidence: {response['score']:.4f}")
    print()
    return response['answer']

# Example questions
# Questions = input("Enter your Query: ")
# prints(Questions)

st.title("Health Suggestions ;)")

# User Input
query = st.text_input("Enter your query:")

# Processing the Input
if st.button("Process"):
    # Call the Python file to process the query
    result = prints(query)
    st.write("Processed Result:")
    st.write(result)

