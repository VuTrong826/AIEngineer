from basemodel.schemas import ReviewAnalysis
import ollama

MODEL_NAME = "qwen3:1.7b"
client = ollama.Client()
def pydantic_output(review : str) -> str:
    response = client.chat(
        model = MODEL_NAME,
        think=False,
        options= {
            "num_predict" : 1024
        },
        messages = [
            {
                "role" : "system",
                "content" : "Bạn phân tích review sản phẩm. Trả về sentiment, rating từ 1 đến 5 và danh sách keywords."
            },
            {
                "role" : "user",
                "content" : review
            }
        ],
        format = ReviewAnalysis.model_json_schema(),
    )
    gen = response["message"]["content"]
    result = ReviewAnalysis.model_validate_json(gen)
    return result
def main():
    review = "Giao hàng siêu nhanh, đóng gói đẹp, nhưng pin hơi yếu."
    result = pydantic_output(review)
    print(result.model_dump_json(indent =2))
    
if __name__ == "__main__":
    main()
    