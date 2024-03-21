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


def create_or_update_organization_secret_github(organization: str, secret_name: str):
    """
    Create or update org level secret in GitHub
    Ref https://docs.github.com/en/rest/actions/secrets?apiVersion=2022-11-28#create-or-update-an-organization-secret

    The token must have the following permission set: organization_secrets:write
    """
    encrypted_secret = os.getenv('ENCRYPTED_SECRET')
    if not encrypted_secret:
        print("ENCRYPTED_SECRET environment variable is not set or is empty.")
    print(f'encrypted sec is: {encrypted_secret}')
    ist_now_formatted = current_ist_time()
    github_org_secret_endpoint = f"https://api.github.com/orgs/{organization}/actions/secrets/{secret_name}"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    data = {
        "encrypted_value": encrypted_secret,
        "visibility": "all",
        "key_id": os.getenv('PUBLIC_KEY_ID')
    }
    response = requests.put(github_org_secret_endpoint, headers=headers, json=data)
    if response.status_code == '201':
        print(f"Secret {secret_name} created {organization} at {ist_now_formatted} ")
    else:
        print(f"Secret {secret_name} updated on {organization} at {ist_now_formatted} ")


def main():
    """To test the code"""
    # Configuring to read ENCRYPTED_SECRET
    # encrypted_secret = os.getenv('ENCRYPTED_SECRET')
    # organization = 'devwithkrishna'
    # secret_name = 'noidea'
    organization = os.getenv('organization')
    secret_name = os.getenv('secret_name')

    # Function call
    create_or_update_organization_secret_github(organization, secret_name)

if __name__ == "__main__":
    main()