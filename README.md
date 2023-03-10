# test-utility-scripts

## Pre-requiste:
Prior to mirroring releases, source repo needs to be mirrored to target repo
1. Create a new TARGET_REPOSITORY repo eg:'setup-node' in your org of choice via GUI
2. In your terminal enter "git clone --bare https://github.com/EXAMPLE-ORG/SOURCE-REPOSITORY.git"
3. cd SOURCE-REPOSITORY.git
4. git push --mirror https://github.com/EXAMPLE-USER/TARGET-REPOSITORY.git"
5. cd ..
6. rm -rf SOURCE-REPOSITORY.git

Now your TARGET-REPOSITORY is ready in GitHub

## Test scripts for creating releases in a target repo based on source repo releases 

For testing aop migration utility there is a need to mirror the releases from source repo to target repo. Using create-release.py this can be achieved programmatically

1. git clone the repository ('gh repo clone actions-on-packages/test-utility-scripts')
2. cd into repo
3. pip3 install -r requirements.txt
4. update ACCESS_TOKEN with ur PAT_TOKEN(SSO_ENABLED), source_repo_url, target_repo_url referring comments in the create-release.py
5. python3 create-release.py
