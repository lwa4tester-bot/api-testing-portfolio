import requests

update = {
    "title": "fake",
    "body": "It's just a fake!!!",
    "userId": 999
} 

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.put(url, json=update)
data = response.json()

print(f"Status code: {response.status_code}")
print(f"New title: {data['title']}")