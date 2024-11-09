import requests
import json


def send_push_notification(device_token, otp):
    url = "https://fcm.googleapis.com/fcm/send"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=YOUR_SERVER_KEY'  # Replace with your Firebase server key
    }
    data = {
        "to": device_token,
        "notification": {
            "title": "Your OTP Code",
            "body": f"Your OTP is: {otp}",
            "priority": "high"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()


# Example usage
device_token = "USER_DEVICE_TOKEN"  # Replace with the actual device token
otp = generate_otp(secret)
response = send_push_notification(device_token, otp)
print(response)
