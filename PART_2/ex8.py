#Schema - enforced JSON with Ollama SDK
import ollama
import json

MODEL_NAME = "qwen3:1.7b"

client = ollama.Client()

def scheme_output(review : str ) -> str :
    response = client.chat(
        model = MODEL_NAME,
        think= False,
        options= {
            "num_predict" :  1024
        },
        messages= [
            {
                "role" : "user",
                "content" : f"Trích xuất thông tin từ review (rating từ 1 đến 5): {review}",
            },

        ],
        format = {
            "type" : "object",
            "properties" : {
                "sentiment" : {"type" : "string", "enum" : ["positive" ,"negative","neutral"]},
                "rating" : {"type": "integer"},
                "keywords" : {"type" : "array","items": {"type" : "string"}},
            },
            "required" : ["sentiment","rating","keywords"],
            "additionalProperties" : False
        }
    )
    return response["message"]["content"]

if __name__ == "__main__":
    gen = scheme_output(review = "Giao hàng siêu nhanh, đóng gói đẹp, nhưng pin hơi yếu.")
    text = gen
    data = json.loads(text)
    print(json.dumps(data, ensure_ascii = False, indent = 2))