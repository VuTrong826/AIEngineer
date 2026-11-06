from ollama import Client
from Schema.schema import Ticket
MODEL_NAME = "qwen3:1.7b"

def generator(raw_text : str) -> Ticket : 
    client = Client(
        host = "http://localhost:11434"
    )
    response = client.chat(
        model= MODEL_NAME,
        messages = [
            {
                "role" : "system",
                "content" : "Bạn là trợ lý tạo ticket hỗ trợ. Chỉ trả về JSON đúng schema."
            },
            {
                "role" : "user",
                "content" : f"Tạo một ticket từ mô tả sau: {raw_text}"
            }
        ],
        format = Ticket.model_json_schema(),
        options= {
            "temperature" : 0.1,
            "num_predict" : 1024
        }
    )
    return Ticket.model_validate_json(response.message.content)

if __name__ == "__main__":
    raw_text = "Nút thanh toán bị lỗi, khách không mua được — cần sửa gấp!"
    ticket = generator(raw_text)
if __name__ == "__main__":
    raw_text = "Nút thanh toán bị lỗi, khách không mua được — cần sửa gấp!"
    ticket = generator(raw_text)
    print(ticket.model_dump_json(indent=2, ensure_ascii=False))