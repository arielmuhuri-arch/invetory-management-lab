import requests

BASE_URL = "http://127.0.0.1:5000"


while True:

    print("\nInventory Manager")

    print("1. View Items")
    print("2. Add Item")
    print("3. Search Barcode")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        response = requests.get(BASE_URL + "/items")

        print(response.json())

    elif choice == "2":

        name = input("Name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        requests.post(
            BASE_URL + "/items",
            json={
                "name": name,
                "quantity": quantity,
                "price": price
            }
        )

        print("Added!")

    elif choice == "3":

        barcode = input("Barcode: ")

        response = requests.get(BASE_URL + "/search/" + barcode)

        print(response.json())

    elif choice == "4":

        break