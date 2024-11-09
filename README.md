# Secure OTP Verification System

## Overview

This project implements a high-security OTP (One-Time Password) verification mechanism using **TOTP (Time-based One-Time Password)** for enhanced security. The system integrates features such as **encrypted OTP storage**, **push notifications**, **rate-limiting**, and **multi-factor authentication (MFA)** to provide a secure solution for user authentication.

## Features

- **Time-based OTP (TOTP)** generation using `pyotp` library.
- **Encrypted OTP secret** storage using `cryptography` library (AES encryption).
- **Push notifications** for secure OTP delivery (Firebase Cloud Messaging).
- **Rate limiting** to prevent brute-force attacks.
- **OTP expiration** with a short validity window (30-60 seconds).
- **Key rotation** to prevent long-term exposure of OTP secrets.
- Optional integration with **multi-factor authentication (MFA)** using biometrics or hardware tokens.

## Technologies Used

- **Python** (for backend and OTP generation)
- **pyotp** (for generating TOTP)
- **cryptography** (for encrypting OTP secrets)
- **Firebase Cloud Messaging (FCM)** (for OTP push notifications)
- **Flask-Limiter** (for rate-limiting requests)
- **reCAPTCHA** (for CAPTCHA implementation to prevent automated brute-force attacks)

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Clone the repository

```bash
git clone https://github.com/yourusername/secure-otp-system.git
cd secure-otp-system
