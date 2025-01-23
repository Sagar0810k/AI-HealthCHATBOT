import streamlit as st # type: ignore
import nltk # type: ignore
from transformers import pipeline # type: ignore
from nltk.corpus import stopwords # type: ignore
from nltk.tokenize import word_tokenize # type: ignore

chatbot =pipeline("text-generation",model='distilgpt2')

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        return "It is prescribed to take medication."
    else:
        # Use the chatbot for generating a response with adjusted parameters
        response = chatbot(user_input, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)
    
    return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Health Care Assistant: ", response)
        else:
            st.write("Please enter a message.")
 
main()
