import unittest
import requests
import responses


localUrl = "http://127.0.0.1:8000/shippingOptions"


mockResponse = {
    "shipping_options": [
        {"name": "Option 1", "type": "Delivery", "cost": 10, "estimated_days": 5},
        {"name": "Option 2", "type": "Custom", "cost": 5, "estimated_days": 3},
        {"name": "Option 3", "type": "Pickup", "cost": 7, "estimated_days": 2},
    ]
}


class TestMain(unittest.TestCase):
    @responses.activate
    def test_simple(self):
        responses.add(
            responses.GET,
            "http://127.0.0.1:8000/shippingOptions",
            json={"error": "not found"},
            status=404,
        )
        resp = requests.get("http://127.0.0.1:8000/shippingOptions")

        self.assertEqual(resp.json(), {"error": "not found"})

        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].response.text, '{"error": "not found"}')
        self.assertEqual(
            responses.calls[0].request.url, "http://127.0.0.1:8000/shippingOptions"
        )

    @responses.activate
    def test_simple(self):
        responses.add(
            responses.GET,
            "http://127.0.0.1:8000/shippingOptions",
            json=[
                {"name": "Option 2", "type": "Custom", "cost": 5, "estimated_days": 3},
                {"name": "Option 3", "type": "Pickup", "cost": 7, "estimated_days": 2},
                {
                    "name": "Option 1",
                    "type": "Delivery",
                    "cost": 10,
                    "estimated_days": 5,
                },
            ],
            status=200,
        )
        resp = requests.get("http://127.0.0.1:8000/shippingOptions")

        self.assertEqual(
            resp.json(),
            [
                {"name": "Option 2", "type": "Custom", "cost": 5, "estimated_days": 3},
                {"name": "Option 3", "type": "Pickup", "cost": 7, "estimated_days": 2},
                {
                    "name": "Option 1",
                    "type": "Delivery",
                    "cost": 10,
                    "estimated_days": 5,
                },
            ],
        )

        self.assertEqual(
            responses.calls[0].request.url, "http://127.0.0.1:8000/shippingOptions"
        )


if __name__ == "__main__":
    unittest.main()
