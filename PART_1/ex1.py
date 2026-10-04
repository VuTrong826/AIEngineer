import os
from dotenv import load_dotenv

#load key/value from .env
load_dotenv()

#read the key from the enviroment - never hardcode it in source
api_key = os.environ["ANTHROPIC_API_KEY"]
#hien thi ra do dai cua key
print("Da nap API key, do dai ", len(api_key))

