import requests
from requests.exceptions import RequestException

BASE_URL = "http://127.0.0.1:5000"


def handle_request(request_func, *args, **kwargs):
    try:
        response = request_func(*args, **kwargs)
        response.raise_for_status()
        return response
    except RequestException as error:
        print("Error connecting to the inventory server:", error)
        return None


while True:
    print("\nInventory Manager")
    print("1. View Items")
    print("2. Add Item")
    print("3. Search Barcode")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        response = handle_request(requests.get, BASE_URL + "/items")
        if response:
            print(response.json())

    elif choice == "2":
        name = input("Name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        response = handle_request(
            requests.post,
            BASE_URL + "/items",
            json={
                "name": name,
                "quantity": quantity,
                "price": price
            }
        )
        if response:
            print("Added!", response.json())

    elif choice == "3":
        barcode = input("Barcode: ")
        response = handle_request(requests.get, BASE_URL + "/search/" + barcode)
        if response:
            print(response.json())

    elif choice == "4":
        break
