import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY_HERE"

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")