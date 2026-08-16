import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

print(f"Users: {users}")

# 1. Minden felhasználó neve (name mező) egy listában
names = [user["name"] for user in users]
print("All names:", names)

# 2. Csak azok a városok, ahol a lakcím (address.city) tartalmazza az "burgh" szót
cities_with_burgh = [user["address"]["city"] for user in users if "burgh" in user["address"]["city"]]
print("Cities containing 'burgh':", cities_with_burgh)

# 3. kigyűjti azoknak a felhasználóknak a cégnevét (company.name), akiknek a website mezője .org-ra végződik
# Használd a .endswith() metódust

company_with_dot_org = [user["company"]["name"] for user in users if user["website"].endswith(".org")]
print(f"Companies with .org website: {company_with_dot_org}")
