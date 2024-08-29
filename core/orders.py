import requests

class Orders:
    def __init__(self, restaurant_id, token):
        self.base_url = "https://toast-api-server/orders/v2"
        self.headers = {
            "Toast-Restaurant-External-ID": restaurant_id,
            "Authorization": f"Bearer {token}"
        }

    def fetch_orders_bulk(self, business_date, start_date, end_date, page=0, page_size=0):
        url = f"{self.base_url}/ordersBulk"
        query = {
            "businessDate": business_date,
            "startDate": start_date,
            "endDate": end_date,
            "page": str(page),
            "pageSize": str(page_size)
        }
        response = requests.get(url, headers=self.headers, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
            