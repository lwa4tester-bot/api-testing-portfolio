import requests
import json

# response = requests.get("https://jsonplaceholder.typicode.com/users/1")
# data = response.json()

# print(json.dumps(data, indent=2))

res1 = requests.get("https://jsonplaceholder.typicode.com/posts/5")
data1 = res1.json()

user_id = data1["userId"]

res2 = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
data2 = res2.json()

email = data2["email"]
company_name = data2["company"]["name"]


res3 = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
data3 = res3.json()


# all_posts = [post for post in data3 if post["userId"] == user_id]

print(f"Post author's email: {email}")
print(f"Post author's company: {company_name}")
print(f"Number of posts by this author: {len(data3)}")




