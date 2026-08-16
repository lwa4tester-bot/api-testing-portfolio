import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 2})

posts = response.json()

print("Number of posts:", len(posts))

for post in posts:
    print(post["title"])