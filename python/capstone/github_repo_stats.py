"""
This script analyzes a specified GitHub user's public profile and repositories using the GitHub API.
After authenticating via a token, it fetches all public repositories in a paginated loop while handling potential
HTTP and connection errors.
Finally, it calculates the total star count, identifies the most popular repository, and lists 
all unique programming languages used.
"""

import requests
import os
import sys

from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")


base_url = "https://api.github.com/users/"
username = "sindresorhus"

# Displays a specific message for known HTTP error codes and then exits the script.
def handle_http_error(response):
    # 404: Not Found
    if response.status_code == 404:
        print("User not found.")
    
    # 401: Unauthorized
    elif response.status_code == 401:
        print("Unauthorized access")
    
    # 403: Forbidden
    elif response.status_code == 403:
        print("API rate limit exceeded")
    
    # Other HTTP errors
    else:
        print("HTTP error")
    
    sys.exit() 

    

try:
    response = requests.get(f"{base_url}{username}",
                        # Authorization is required to raise the rate limit. 
                        headers={"Authorization": f"Bearer {github_token}"}) 
    response.raise_for_status()

except requests.HTTPError:
     handle_http_error(response)



# non-specific connection error
except requests.exceptions.ConnectionError:
    print("Connection error!")
    sys.exit()


profile_data = response.json()
repos_count = profile_data['public_repos']
print(f"Public repos: {repos_count}")

page = 1
all_repos = []

try:
    # Request 100 repos per page.
    while True:
        params = {
            "per_page":100,
            "page":page
        }
        response = requests.get(f"{base_url}{username}/repos",
                        params=params,
                        # Authorization is required to raise the rate limit.
                        headers={"Authorization": f"Bearer {github_token}"}) 
        response.raise_for_status()

        repos = response.json()
        all_repos.extend(repos)

        # Break when number of given repos is less than 100
        if len(repos) < 100:
            break
        page += 1
except requests.exceptions.HTTPError:
    handle_http_error(response)

# non-specific connection error     
except requests.exceptions.ConnectionError:
    print("Connection error!")
    sys.exit()


print(f"Repos fetched: {len(all_repos)}")

all_stars = [r['stargazers_count'] for r in all_repos]

max_stars = max(all_stars)
best_repos = [(r['name'],r['stargazers_count']) for r in all_repos if r['stargazers_count'] == max_stars]

print(f"All stars: {sum(all_stars)}")
print(f"Best repo(s): {best_repos[0][0]} with {max_stars} stars")

unique_languages = {r['language'] for r in all_repos if r['language'] is not None}


print(f"Unique languages used: {len(unique_languages)}")
print(f"Programming languages: {','.join(sorted(unique_languages))}")