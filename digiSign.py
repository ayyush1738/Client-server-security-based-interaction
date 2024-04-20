import sys
import hashlib
import os
from Crypto import DSA
from Crypto import DSS
from Crypto import SHA1

def generate_digital_signature(file_name):
    # Generate a DSA signature
    try:
        # Generate a key pair
        key = DSA.generate(1024)
        priv = key.export_key()
        pub = key.public_key().export_key()

        # Create a signature object and initialize it with the private key
        signer = DSS.new(key, 'fips-186-3')

        # Read the data to be signed
        with open(file_name, 'rb') as f:
            data = f.read()

        # Generate the signature
        h = SHA1.new(data)
        signature = signer.sign(h)

        # Save the signature in a file
        with open("signature.txt", "wb") as f:
            f.write(signature)

        # Save the public key in a file
        with open("publickey.txt", "wb") as f:
            f.write(pub)

    except Exception as e:
        print("Caught exception:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "sign.txt")
        sys.exit(1)

    file_name = sys.argv[1]

    generate_digital_signature(file_name)
