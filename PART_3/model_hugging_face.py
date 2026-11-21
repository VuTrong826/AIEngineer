import os
import requests
from dotenv import load_dotenv

load_dotenv()

r = requests.get(
    "https://router.huggingface.co/v1/models",
    headers={"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"},
)
r.raise_for_status()
for m in r.json()["data"][:50]:
    print(m["id"])











