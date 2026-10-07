import unittest

from app import app


class CatalogTests(unittest.TestCase):
    def test_original_catalog_and_browser_access(self):
        response = app.test_client().get("/products", headers={"Origin": "https://example.azurestaticapps.net"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [
            {"id": 1, "name": "Dog Food", "price": 19.99},
            {"id": 2, "name": "Cat Food", "price": 34.99},
            {"id": 3, "name": "Bird Seeds", "price": 10.99},
        ])
        self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")

    def test_catalog_cannot_be_modified(self):
        self.assertEqual(app.test_client().post("/products", json={}).status_code, 405)


if __name__ == "__main__":
    unittest.main()
