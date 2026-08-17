import requests
import sys

username = input("Give me a GitHub username: ")
github_url = "https://api.github.com/users/"

try:
    response = requests.get(f"{github_url}{username}")
    response.raise_for_status()
except requests.HTTPError: 
    print("User not found.")
    sys.exit()
except requests.exceptions.ConnectionError:
    print("Connection error!")
    sys.exit()
    
data = response.json()

def write_info(data):
    print()
    name = data['name'] if data['name'] is not None else "<no info>"
    print(f"Username: {name}")
    bio = data['bio'] if data['bio'] is not None else "<no info>"
    print(f"Bio: {bio}")
    print(f"Public repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
    print(f"Created at {data['created_at']}")

write_info(data)








