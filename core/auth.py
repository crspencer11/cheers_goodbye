import requests

class Authenticator:
    auth_url = "https://your-toast-authentication-endpoint.com/authentication/login"

    def __init__(self, client_id: str, client_secret: str, access_type: str):
        self.client_id = client_id
        self.slient_secret = client_secret
        self.access_type = access_type


    def authenticate(self):
        payload = {
            "clientId": self.client_id,
            "clientSecret": self.client_secret,
            "userAccessType": self.access_type
        }
        response = requests.post(self.auth_url, json=payload)
        if response.status_code == 200:
            auth_data = response.json()
            access_token = auth_data['token']['accessToken']
            print(f"Access Token: {access_token[:4]}****")
        else:
            print("Failed to authenticate:", response.status_code, response.text)
