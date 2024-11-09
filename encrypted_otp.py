from cryptography.fernet import Fernet

# Generate a key for AES encryption (store this key securely)
def generate_encryption_key():
    return Fernet.generate_key()

# Encrypt the secret before storing it
def encrypt_secret(secret, key):
    cipher = Fernet(key)
    encrypted_secret = cipher.encrypt(secret.encode())
    return encrypted_secret

# Decrypt the secret when needed for OTP generation
def decrypt_secret(encrypted_secret, key):
    cipher = Fernet(key)
    decrypted_secret = cipher.decrypt(encrypted_secret).decode()
    return decrypted_secret

# Example usage
key = generate_encryption_key()
encrypted_secret = encrypt_secret(secret, key)
decrypted_secret = decrypt_secret(encrypted_secret, key)
print(f"Encrypted Secret: {encrypted_secret}")
print(f"Decrypted Secret: {decrypted_secret}")



import random

# Function to rotate the secret key after N OTP generations or time
def rotate_key():
    # Example: Replace the current key with a new randomly generated one
    new_secret = pyotp.random_base32()
    return new_secret
