import requests

ACCESS_TOKEN = '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'
source_repo_url = 'https://api.github.com/repos/actions/setup-node/releases?per_page=100'
target_repo_url = 'https://api.github.com/repos/vinay-personal-org/setup-node/releases'
headers = {
    'Authorization': 'token ' + ACCESS_TOKEN,
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(source_repo_url, headers={'Authorization': 'token ' + ACCESS_TOKEN})
#print(response.json())
releases_list = response.json()
num_releases = len(releases_list)

#iterate releases_list from source repo and create releases in target repo

for release in releases_list:
     if release['draft'] == True:
         print("found a draft release with tag " + str(release['tag_name']) + " hence skipping it")
     else:
        tag_name = release['tag_name']
        target_commitish = release['target_commitish']
        name = release['name']
        description = release['body']
        draft = release['draft']
        prerelease = release['prerelease']
        generate_release_notes = False
        payload = {"tag_name": tag_name, "target_commitish": target_commitish, "name": name, "body": description, "draft": draft, "prerelease": prerelease, "generate_release_notes": generate_release_notes}
        response = requests.post(target_repo_url, headers=headers, json=payload)
        if response.status_code not in [200, 201, 422] :
         print("something went wrong during release creation of tag " + str(tag_name) + " with status code " + str(response.status_code) + ".Hence aborting the process")

print("All releases created")

