
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

MODEL_NAME = "llama3.2:3b"

def huggingface_llm(prompt : str) -> str :
    response = client.chat.completions.create(
        model = MODEL_NAME,
        messages = [
            {
                "role" : "user",
                "content" : prompt
            }
        ],
        max_tokens= 1024
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(huggingface_llm("Giải thích RAG trong 2 câu, dễ hiểu cho dev."))
