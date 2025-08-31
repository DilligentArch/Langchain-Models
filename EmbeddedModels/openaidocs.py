from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embeddings=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents=[
    "Paris is the capital of France.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome."
]

result=embeddings.embed_documents(documents)

print(str(result))