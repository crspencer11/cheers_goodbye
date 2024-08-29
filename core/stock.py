import requests

class CurrentStock:
    def __init__(self, restaurant_id: str, token: str):
        self.base_url = "https://toast-api-server/stock/v1/inventory"
        self.headers = {
            "Toast-Restaurant-External-ID": "string",
            "Authorization": "Bearer <YOUR_TOKEN_HERE>"
        }

    