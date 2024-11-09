from flask import Flask, request
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/verify_otp', methods=['POST'])
@limiter.limit("5 per minute")  # Limit to 5 requests per minute
def verify_otp():
    otp_input = request.form['otp']
    # Add OTP validation logic here
    return "OTP Verified" if otp_input == otp else "Invalid OTP"

if __name__ == '__main__':
    app.run(debug=True)
