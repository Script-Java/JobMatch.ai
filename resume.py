import streamlit as st
import pdfplumber
from openai import OpenAI


class ResumeTweaker:
    def __init__(self, resume, key):
        self.resume = resume
        self.key = key
        self.client = OpenAI(api_key=self.key)
        
    # Convert resume to text here then return it
    
    def resume_to_text(self):
        with pdfplumber.open(self.resume) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages])
            return text
    
    def ai_tweaker(self):
        response = self.client.chat.completions.create(
            model = "gpt-4-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful AI data analyst."},
                {"role": "user", "content": ""}
            ]
        )
        return response.choices[0].message.content
    
