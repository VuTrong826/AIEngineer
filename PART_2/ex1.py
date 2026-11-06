from ollama import Client
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from prompt_engineer.prompt import system_prompt
MODEL_NAME = "qwen3:1.7b"

def generator(text: str) ->  str:
    client = Client(
        host = "http://localhost:11434"
    )
    response = client.chat(
    model = MODEL_NAME,
    messages =[
        {
            "role" : "system",
            "content" : system_prompt
        },
        {
            "role" : "user",
            "content": text
        }
    ],
    options= {
        "temperature" : 0.1,
        "num_predict" : 1024
    }
    )
    return response["message"]["content"]

if __name__ == "__main__":
    text = "ACME công bố doanh thu quý 4 đạt 12 tỷ, tăng 30% so với cùng kỳ..."
    print(generator(text))
    