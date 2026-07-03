import unittest

from app import app


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_add_item(self):

        response = self.client.post(
            "/items",
            json={
                "name": "Apple",
                "quantity": 10,
                "price": 50
            }
        )

        self.assertEqual(response.status_code, 201)

    def test_get_items(self):

        response = self.client.get("/items")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()