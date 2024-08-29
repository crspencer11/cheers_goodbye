import os
from auth import Authenticator
from orders import Orders

def main():
    auth_actor = Authenticator(client_id=os.getenv("CLIENT_ID"),
                               client_id=os.getenv("CLIENT_SECRET"),
                               client_id=os.getenv("ACCESS_TYPE"))
    token = auth_actor.authenticate
    orders = Orders(client_id=os.getenv("RESTAURANT_ID"),
                    token=token)
    
    # one weeks worth test
    orders.fetch_orders_bulk(business_date="20240828",
                             end_date="2024-08-27T14:13:12.000+0400",
                             page=0,
                             page_size=0,
                             start_date="2024-08-20T14:13:12.000+0400")

if __name__ == "__main__":
    main()