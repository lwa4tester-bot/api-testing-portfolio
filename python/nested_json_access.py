import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
user = response.json()

print(user["address"]["city"])           # beágyazott objektum
print(user["address"]["geo"]["lat"])      # kétszer beágyazott
print(user["company"]["name"])