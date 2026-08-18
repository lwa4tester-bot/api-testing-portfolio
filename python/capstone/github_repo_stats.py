import requests
import os
import sys

from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")


base_url = "https://api.github.com/users/"
username = "sindresorhus"

try:
    res = requests.get(f"{base_url}{username}",
                        headers={"Authorization": f"Bearer {github_token}"})
    res.raise_for_status()

except requests.HTTPError:

    if res.status_code == 404:
        print("User not found.")
    elif res.status_code == 401:
        print("Unauthorized access")
    elif res.status_code == 403:
        print("API rate limit exceeded")
    else:
        print("HTTP error")

    sys.exit() 

except requests.exceptions.ConnectionError:
    print("Connection error!")
    sys.exit()


data = res.json()
repos_count = data['public_repos']
print(f"Public repos: {repos_count}")

i = 1
all_repos = []

try:
    while True:
        params = {
            "per_page":100,
            "page":i
        }
        res = requests.get(f"{base_url}{username}/repos",
                        params=params,
                        headers={"Authorization": f"Bearer {github_token}"}) 
        res.raise_for_status()

        repos = res.json()
        all_repos.extend(repos)

        if len(repos) < 100:
            break
        i += 1
except requests.exceptions.HTTPError:
       
       if res.status_code == 404:
           print("User not found.")
       elif res.status_code == 401:
            print("Unauthorized access")
       elif res.status_code == 403:
            print("API rate limit exceeded")
       else:
            print("HTTP error")
    
       sys.exit() 
       
except requests.exceptions.ConnectionError:
    print("Connection error!")
    sys.exit()


print(f"Repos fetched: {len(all_repos)}")

all_stars = [r['stargazers_count'] for r in all_repos]

max_all_star = max(all_stars)
best_repo = [(r['name'],r['stargazers_count']) for r in all_repos if r['stargazers_count'] == max_all_star]

print(f"All stars: {sum(all_stars)}")
print(f"Best repo: {best_repo[0][0]} with {max_all_star} stars")

unique_languages = {r['language'] for r in all_repos if r['language'] is not None}


print(f"Unique languages used: {len(unique_languages)}")
print(f"Programming languages: {','.join(sorted(unique_languages))}")








