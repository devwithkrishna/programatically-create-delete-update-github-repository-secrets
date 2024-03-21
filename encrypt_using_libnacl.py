# Python script includes a function, encrypt, designed to encrypt Unicode strings using public-key cryptography through the PyNaCl library.
# To utilize this functionality, begin by importing the necessary libraries with the from base64 import b64encode and from nacl import encoding,
# public statements. Subsequently, define and call the encrypt function, passing a Base64-encoded public key and a Unicode string as parameters.
# The function then encrypts the provided value using the public key and returns the result in a Base64-encoded format.
# For example, calling encrypt("aSBhbSBrcmlzaG5hZGhhcwo=", "aSBhbSBrcmlzaG5hZGhhcwo=") demonstrates how to encrypt a sample Unicode string using a specified public key.
# Ensure proper handling and security of public keys and secret values within your application.

from base64 import b64encode
from nacl import encoding, public
import os

def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")

def main():
    repo_public_key = os.environ.get("PUBLIC_KEY")
    secret_value = os.environ.get("SECRET_VALUE")
    # public_key = "<public key here for local testing>"
    # secret_value = "Krishnadhas"

    if not (repo_public_key and secret_value):
        print("Please set REPOSITORY_PUBLIC_KEY and SECRET_VALUE environment variables.")
        exit(1)

    try:
        encrypted_secret = encrypt(repo_public_key, secret_value)
        os.system(f'echo "ENCRYPTED_SECRET={encrypted_secret}" >> $GITHUB_ENV')
        print(f"Encrypted Secret: {encrypted_secret}")
        print(f"Encrypted secret added as a environment variable")
        return encrypted_secret
    except Exception as e:
        print(f"Error encrypting secret: {e}")
        exit(1)

if __name__ == "__main__":
    main()