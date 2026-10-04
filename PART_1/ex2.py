import os 
from dotenv import load_dotenv
from anthropic import Anthropic
from ollama import Client

#load api key from .env
load_dotenv()

MODEL_NAME = "qwen3:1.7b"

#create the client
client = Client(
    host = "http://localhost:11434"
)

response = client.chat(
    model = MODEL_NAME,
    messages = [
        {
            "role" : "user",
            "content" : "Xin chao Ollama ! Hay tra loi mot cau ngan de xac nhan ket noi"

        }
    ],
    options = {
        "num_predict" : 500,
        "top_p" : 0.8,
        "temperature" : 0.2
    }
)
print(response.message.content)
print(
    "Token vao:",
    response.prompt_eval_count,
    "| Token ra:",
    response.eval_count
)
