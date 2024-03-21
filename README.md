# programatically-create-delete-update-github-repository-secrets
programatically-create-delete-update-github-repository-secrets

# Pre requesites
* Personal Access Token (PAT) is the recommended way to authenticate. In this demo PAT is USED.
* You can generate a new one from Github settings
* You need to encrypt a secret before you can create or update secrets.


# How code works for create or update a repository secret

* First this will execute the `get_repository_public_key.py` `python program` to get the Organization public key and public key id
    *  This public key is required and used for encryption of secret
    * This public key id is required at time of creation or updation of secret

    `Reference`: [get-a-repository-public-key](https://docs.github.com/en/rest/actions/secrets?apiVersion=2022-11-28#get-a-repository-public-key)


* Then the `python program` `encrypt_using_libnacl` this uses the public key from step 1 and encrypts the secret 
using the prefered method by GitHub.

    `Reference`: [create-or-update-a-repository-secret](https://docs.github.com/en/rest/actions/secrets?apiVersion=2022-11-28#create-or-update-a-repository-secret)

    - Reference used for encryption : [example-encrypting-a-secret-using-python](https://docs.github.com/en/rest/guides/encrypting-secrets-for-the-rest-api?apiVersion=2022-11-28#example-encrypting-a-secret-using-python )

* Then `Python program` `create_or_update_repo_secret` is used to take the public key id from above step and encrypted secret value to create or update the secret.

| status code | operation                |
|-------------|--------------------------|
| 201  | Response when creating a repository secret |
| 204  | Response when updating a secret repository secret   |



## Inputs of workflow

| input name | description|
|------------|------------|
| organization | name of github organization |
| repository_name | name of github repo where secret need to be created |
| secret_name | organization Secret name |
| secret_value | Secret value |


# # How code works for deleting an repository secret

* This runs the `python program` `delete_repo_secret.py` which takes 3 inputs from github workflow 
1. organization name
2. repository name 
3. secret name

* Then deletes the secret

| input | description| 
|-------|--------------|
| organization | GitHub Organization name |
| repository_name | name of github repo where secret need to be created |
| secret_name | Secert to be deleted |