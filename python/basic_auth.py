import requests

response = requests.get(
    "https://postman-echo.com/basic-auth",
    auth=("postman", "password")
)

print("Status code:", response.status_code)
print("Response:", response.json())