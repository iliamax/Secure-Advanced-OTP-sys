import pyotp
import time

# Generate a new secret key for the user (keep this secret safe)
def generate_secret():
    totp = pyotp.TOTP(pyotp.random_base32())  # Generate a new random secret
    return totp.secret

# Generate OTP based on the secret
def generate_otp(secret):
    totp = pyotp.TOTP(secret)
    otp = totp.now()  # OTP will be valid for 30 seconds by default
    return otp

# Example Usage
secret = generate_secret()
print(f"Secret: {secret}")
otp = generate_otp(secret)
print(f"Generated OTP: {otp}")
