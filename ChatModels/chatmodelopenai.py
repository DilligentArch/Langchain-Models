from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPEN_AI_Key")

model=ChatOpenAI(model='gpt-4',temperature=0.7,max_completion_tokens=10, api_key=api_key)

result=model.invoke("What is the capital of France?")

print(result.content)