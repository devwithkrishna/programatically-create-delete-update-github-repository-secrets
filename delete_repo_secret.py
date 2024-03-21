import requests
import os
from datetime import datetime
import pytz

def current_ist_time():
    """code to return time in IST"""
    # Get the current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    ist_now = datetime.now(ist)

    # Format and print the current time in IST
    ist_now_formatted = ist_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return ist_now_formatted


def delete_repository_secret_github(organization: str, repository_name:str, secret_name: str):
    """
    Create or update org level secret in GitHub
    Ref https://docs.github.com/en/rest/actions/secrets?apiVersion=2022-11-28#create-or-update-an-organization-secret

    The token must have the following permission set: organization_secrets:write
    """
    ist_now_formatted = current_ist_time()
    github_repo_secret_endpoint = f"https://api.github.com/repos/{organization}/{repository_name}/actions/secrets/{secret_name}"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.delete(github_repo_secret_endpoint, headers=headers)
    if response.status_code == 204:
        print(f"Secret {secret_name} deleted from {repository_name} at {ist_now_formatted} ")
    else:
        print(f"Something happened while deleting {secret_name} from {repository_name} at {ist_now_formatted} ")


def main():
    """To test the code"""

    organization = os.getenv('organization')
    secret_name = os.getenv('secret_name')
    repository_name = os.getenv('repository_name')

    # Function call
    delete_repository_secret_github(organization,repository_name, secret_name)

if __name__ == "__main__":
    main()