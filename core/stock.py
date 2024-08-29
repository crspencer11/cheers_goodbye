import requests

class CurrentStock:
    def __init__(self, restaurant_id: str, token: str):
        self.base_url = "https://toast-api-server/stock/v1/inventory"
        self.headers = {
            "Toast-Restaurant-External-ID": restaurant_id,
            "Authorization": f"Bearer {token}"
        }

    def get_stock(self, status: str):
        query = {
            "status": status
        }
        response = requests.get(self.base_url, headers=self.headers, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    