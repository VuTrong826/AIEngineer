import ollama
import httpx

client =  ollama.Client(
    host = "http://localhost:11434"
)
MODEL_NAME = "llama3.2:3b"

def generator_llm():
    try:
        response = client.chat(
            model = MODEL_NAME,
            options= {
                "num_predict" : 2048
            },
            messages = [
                {
                    "role" : "system",
                    "content" : "content"
                },
                {
                "role" : "user",
                "content" : "Xin chào"
                }
            ]
                )
        return response["message"]["content"]
    except ollama.ResponseError as e:
        #sever co tra loi nhung bao loi (tuong duong APIstatusError)
        if e.status_code == 404 :
            print(f"chua co model '{MODEL_NAME}'. Chay ollama pull '{MODEL_NAME}'")
        elif e.status_code in (401,403) :
            print(f"bi tu choi truy cap - kiem tra proxy/header xac thuc (neu co)")
        elif e.status_code == 429 :
            print("bi gioi han tan suat (thuong do proxy phia truoc). Cho roi thu lai ")
        elif e.status_code  >= 500 :
            print(f"loi API ({e.status_code}) - thu lai sau ")
        else :
            print(f"Loi API ({e.status_code}): {e.error}")

    except (ConnectionError, httpx.ConnectError):
        #tuong duong APIconnectionError
        print("Khong connect duoc voi ollama - kiem tra da chay chua ( ollama serve)")    
    except httpx.TimeoutException:
        print("Het thoi gian cho - Model cos the dang tai hoac may qua cham")



if __name__ == "__main__":
    print(generator_llm())