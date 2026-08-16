import requests

new_post = {
    "title": "My test post",
    "body": "Testing POST requests with Python",
    "userId": 5
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

print("Status code:", response.status_code)
print("Created post ID:", response.json()["id"])
print("Title:", response.json()["title"])