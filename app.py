from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

inventory = []
next_id = 1

# Home
@app.route("/")
def home():
    return jsonify({"message": "Inventory API Running"})


# Get all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(inventory)


# Get one item
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404


# Add item
@app.route("/items", methods=["POST"])
def add_item():
    global next_id

    data = request.json

    item = {
        "id": next_id,
        "name": data["name"],
        "quantity": data["quantity"],
        "price": data["price"]
    }

    inventory.append(item)
    next_id += 1

    return jsonify(item), 201


# Update item
@app.route("/items/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    data = request.json

    for item in inventory:

        if item["id"] == item_id:

            item["name"] = data.get("name", item["name"])
            item["quantity"] = data.get("quantity", item["quantity"])
            item["price"] = data.get("price", item["price"])

            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404


# Delete item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    for item in inventory:

        if item["id"] == item_id:

            inventory.remove(item)

            return jsonify({"message": "Deleted"})

    return jsonify({"error": "Item not found"}), 404


# External API
@app.route("/search/<barcode>", methods=["GET"])
def search_product(barcode):

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    response = requests.get(url)

    data = response.json()

    if data["status"] == 1:

        product = data["product"]

        return jsonify({
            "product_name": product.get("product_name"),
            "brand": product.get("brands"),
            "category": product.get("categories")
        })

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)