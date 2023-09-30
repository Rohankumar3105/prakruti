!pip install transformers
from transformers import pipeline
import pandas as pd
import stream2
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
def chatbot(question):
    # Provide a context or passage where the answer can be found
    with open("/content/Data.txt", "r", encoding="utf-8") as file:
        context = file.read()
    # Use the question-answering model to find the answer
    answer = qa_pipeline(question=question, context=context)

    return answer
def prints(questions):
    response = chatbot(questions)
    # print(f"Question: {question}")
    # print(f"Answer: {response['answer']}")
    # print(f"Confidence: {response['score']:.4f}")
    # print()
    return response['answer']
# result = prints(stream2.query)
# print(result)
# stream2.receive_data(result)
def question(query):
    result = prints(query)
    return result
