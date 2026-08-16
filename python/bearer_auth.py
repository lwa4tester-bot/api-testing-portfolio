import os
import requests
from dotenv import load_dotenv

load_dotenv()  # beolvassa a .env fájlt

api_key = os.getenv("API_TOKEN")
print(f"Loaded key: {api_key}")

url = "https://postman-echo.com/get"
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(url, headers=headers)
data = response.json()

print(f"Status code: {response.status_code}")
print(f"Authorization header sent: {data['headers']['authorization']}")