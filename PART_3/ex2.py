import ollama

MODEL_NAME = "llama3.2:3b"
client = ollama.Client(host = "http://localhost:11434")

def streaming_llm(text : str) -> str : 
    response = client.chat(
        model = MODEL_NAME,
        options={
            "num_predict" : 2048,
        },
        messages = [
            {
                "role" : "system",
                "content" : "bạn là một chuyên gia viết văn RAG in AI"
            },
            {
                "role" : "user",
                "content": text 
            }
        ],
        stream = True
    )  
    
    full = ""
    for chunk in response:
        piece = chunk["message"]["content"]
        print(piece, end = "", flush = True)
        full += piece
    print()
    return full
        

if __name__ == "__main__":
    streaming_llm("Viết một đoạn 200 chữ về RAG")
