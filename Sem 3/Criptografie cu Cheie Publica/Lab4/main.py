from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class SimpleEncryptor:
    def __init__(self):
        # Setting: The alphabet will have 27 characters.
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

    def generate_key_pair(self):
        # Generates a public key and a private key.
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()

        # Serialize keys to PEM format (Privacy Enhanced Mail)
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return private_pem, public_pem

    def encrypt(self, public_key_pem, plaintext):
        # Load public key
        public_key = serialization.load_pem_public_key(public_key_pem)

        # Encrypt the plaintext
        ciphertext = public_key.encrypt(
            plaintext.encode(),
            padding.OAEP( # Optimal Asymmetric Encryption Padding
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return ciphertext

    def decrypt(self, private_key_pem, ciphertext):
        # Load private key
        private_key = serialization.load_pem_private_key(
            private_key_pem,
            password=None
        )

        # Decrypt the ciphertext
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return plaintext.decode()
    
    def validate(self, plaintext):
        # Check that the plaintext only contains valid characters
        for char in plaintext:
            if char not in self.alphabet:
                raise Exception("Invalid character: " + char)

def main():
    encryptor = SimpleEncryptor()

    # Generate key pair
    private_key_pem, public_key_pem = encryptor.generate_key_pair()

    print("Public Key:")
    print(public_key_pem.decode())

    print("\nPrivate Key:")
    print(private_key_pem.decode())

    # Example plaintext
    plaintext = "HELLO WORLD"
    encryptor.validate(plaintext)

    # Encrypt and decrypt
    ciphertext = encryptor.encrypt(public_key_pem, plaintext)
    decrypted_text = encryptor.decrypt(private_key_pem, ciphertext)

    print("\nOriginal Text:", plaintext)
    print("Encrypted Text:", ciphertext)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()


"""
The security of the ElGamal algorithm relies on the difficulty of the Discrete Logarithm Problem. If an attacker can solve this problem efficiently, they can compute the private key from the public key and decrypt any message encrypted with that public key. However, no efficient algorithm is known for solving the Discrete Logarithm Problem, making ElGamal a secure choice for public-key cryptography, assuming the keys are chosen properly and are of sufficient length.
"""