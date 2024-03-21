import os
import pytz
import requests
import argparse
from datetime import datetime

def current_ist_time():
    """code to return time in IST"""
    # Get the current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    ist_now = datetime.now(ist)

    # Format and print the current time in IST
    ist_now_formatted = ist_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return ist_now_formatted
def get_repository_public_key(organization:str ,repository_name: str):
    """
    Get the ORG name and repo name retrieve the public key of the repository
    :param organization:
    :param repository_name:
    :return:
    """
    repository_public_key_url = f'https://api.github.com/repos/{organization}/{repository_name}/actions/secrets/public-key'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(repository_public_key_url, headers= headers)
    response_json = response.json()
    repository_public_key = response_json['key']
    # print(f'repo public key is {repository_public_key}')
    response_code = response.status_code

    if response_code == 200:
        print(f'Public key for {repository_name} retrieved from {organization} Org Successfully at {current_ist_time()}')
    else:
        print(f'Failed to retrieve public key for {repository_name} retrieved from {organization} Org at {current_ist_time()}')

    return repository_public_key


def get_repository_public_key_id(organization:str ,repository_name: str):
    """
    Get the ORG name and repo name retrieve the public key id of the repository
    :param organization:
    :param repository_name:
    :return:
    """
    repository_public_key_id_url = f'https://api.github.com/repos/{organization}/{repository_name}/actions/secrets/public-key'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(repository_public_key_id_url, headers= headers)
    response_json = response.json()
    repository_public_key_id = response_json['key_id']
    # print(f'repo public key is {repository_public_key_id}')
    response_code = response.status_code

    if response_code == 200:
        print(f'Public key id for {repository_name} retrieved from {organization} Org Successfully at {current_ist_time()}')
    else:
        print(f'Failed to retrieve public key id for {repository_name} retrieved from {organization} Org at {current_ist_time()}')

    return repository_public_key_id


def main():
    """ To test the python code """
    GH_TOKEN = os.environ.get("GH_TOKEN")
    parser = argparse.ArgumentParser(description="Get the public key of the repository in GitHub")
    parser.add_argument("--organization", required=True, type=str, help= "GitHub organization name")
    parser.add_argument("--repository_name", help= "GitHub repository name", type=str, required=True)

    args = parser.parse_args()
    organization = args.organization
    repository_name = args.repository_name

    try:
        repo_public_key = get_repository_public_key(organization, repository_name)
        os.system(f'echo "REPOSITORY_PUBLIC_KEY={repo_public_key}" >> $GITHUB_ENV')
        print(f"Public key added as a environment variable")
        repo_public_key_id = get_repository_public_key_id(organization, repository_name)
        os.system(f'echo "REPOSITORY_PUBLIC_KEY_ID={repo_public_key_id}" >> $GITHUB_ENV')
        print(f"Public key id added as a environment variable")


        # return encrypted_secret
    except Exception as e:
        print(f"Error retrieving public key and public key id of {repository_name}: {e}")
        exit(1)

if __name__ == "__main__":
    main()