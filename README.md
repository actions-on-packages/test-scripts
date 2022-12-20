# test-utility-scripts
Test scripts for creating releases in a target repo based on source repo releases 

For testing migration utility there is a need to mirror the releases from source repo to target repo. Using create-release.py this can be achieved programmatically

1. git clone the repository
2. cd into repo
3. pip3 install -r requirements.txt
4. update ACCESS_TOKEN, source_repo_url, target_repo_url
5. python3 create-release.py
