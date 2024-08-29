import os
from auth import Authenticator
from orders import Orders

def main():
    # Create instances of ClassA and ClassB
    auth_actor = Authenticator(client_id=os.getenv("CLIENT_ID"),
                               client_id=os.getenv("CLIENT_SECRET"),
                               client_id=os.getenv("ACCESS_TYPE"))
    auth_actor.authenticate


if __name__ == "__main__":
    main()