#prompt only 

import json
import ollama

MODEL_NAME = "qwen3:1.7b"
def generator(review : str) -> str:
    client = ollama.Client()
    response = client.chat(
        model= MODEL_NAME,
        options= {
            "num_predict " : 1024
        },
        messages= [
            {
                "role" :  "user",
                "content" :  f'Chỉ trả JSON, KHÔNG giải thích, KHÔNG bọc markdown. '
                             f'Schema : {{"sentiment" : "positive |negative | neutral","rating" : 1-5,"keywords ": []}}'
                            f'Review : {review}'}
        ],
    )
    raw = response["message"]["content"]
    return raw
if __name__ == "__main__":
    gen = generator(review="Giao hàng siêu nhanh, đóng gói đẹp, nhưng pin hơi yếu.")
    print(gen)
    data = json.loads(gen[gen.find("{") : gen.rfind("}") + 1])
    print(data["sentiment"], data["rating"], data["keywords"])