#ZERO_SHOT : YEU CAU THANG, KHONG VI DU
from ollama import Client

MODEL_NAME = "qwen3:1.7b"

system_prompt =   """Phân loại cảm xúc của đánh giá sau là POSITIVE, NEGATIVE hay NEUTRAL.
                    Chỉ trả về một từ.\n\n"""

def zero_shot(user_prompt : str) -> str:
    client = Client(
        host ="http://localhost:11434"
    )
    response = client.chat(
        model= MODEL_NAME,
        messages = [
            {
                "role" : "system",
                "content" : system_prompt
            },
            {
                "role" : "user",
                "content" : user_prompt
            }
        ],
        options= {
            "temperature" : 0.2,
            "top_k" : 200,
            "top_p" :0.8,
            "num_predict" : 1024
        }
    )
    return response["message"]["content"]

def main():
    user_prompt =  "Đánh giá: 'App chạy mượt nhưng hơi tốn pin.'"
    print(zero_shot(user_prompt))

if __name__ == "__main__":
    main()