import unittest
from ShippingOptions import ShippingOptions


class TestShippingOptions(unittest.TestCase):
    def test_same_shipping_costs_and_estimated_delivery_dates(self):
        input = [
            {"name": "Option 1", "type": "Delivery", "cost": 10, "estimated_days": 3},
            {"name": "Option 2", "type": "Custom", "cost": 10, "estimated_days": 3},
            {"name": "Option 3", "type": "Pickup", "cost": 10, "estimated_days": 3},
        ]
        expected = [
            {"name": "Option 1", "type": "Delivery", "cost": 10, "estimated_days": 3},
            {"name": "Option 2", "type": "Custom", "cost": 10, "estimated_days": 3},
            {"name": "Option 3", "type": "Pickup", "cost": 10, "estimated_days": 3},
        ]
        shippingOptions = ShippingOptions(input)
        output = shippingOptions.getSortedOptions()
        self.assertEqual(expected, output)

    def test_same_shipping_costs_different_estimated_delivery_dates(self):
        input = [
            {"name": "Option 1", "type": "Delivery", "cost": 10, "estimated_days": 5},
            {"name": "Option 2", "type": "Custom", "cost": 10, "estimated_days": 2},
            {"name": "Option 3", "type": "Pickup", "cost": 10, "estimated_days": 3},
        ]
        expected = [
            {"name": "Option 2", "type": "Custom", "cost": 10, "estimated_days": 2},
            {"name": "Option 3", "type": "Pickup", "cost": 10, "estimated_days": 3},
            {"name": "Option 1", "type": "Delivery", "cost": 10, "estimated_days": 5},
        ]
        shippingOptions = ShippingOptions(input)
        output = shippingOptions.getSortedOptions()
        self.assertEqual(expected, output)

    def test_same_estimated_delivery_dates_different_shipping_costs(self):
        input = [
            {"name": "Option 1", "type": "Delivery", "cost": 6, "estimated_days": 3},
            {"name": "Option 2", "type": "Custom", "cost": 5, "estimated_days": 3},
            {"name": "Option 3", "type": "Pickup", "cost": 10, "estimated_days": 3},
        ]
        expected = [
            {"name": "Option 2", "type": "Custom", "cost": 5, "estimated_days": 3},
            {"name": "Option 1", "type": "Delivery", "cost": 6, "estimated_days": 3},
            {"name": "Option 3", "type": "Pickup", "cost": 10, "estimated_days": 3},
        ]
        shippingOptions = ShippingOptions(input)
        output = shippingOptions.getSortedOptions()
        self.assertEqual(expected, output)

    def test_both_shipping_costs_and_estimated_delivery_dates_are_different(self):
        input = [
            {"name": "Option 1", "type": "Delivery", "cost": 10, "estimated_days": 5},
            {"name": "Option 2", "type": "Custom", "cost": 5, "estimated_days": 3},
            {"name": "Option 3", "type": "Pickup", "cost": 7, "estimated_days": 2},
        ]
        expected = [
            {"name": "Option 2", "type": "Custom", "cost": 5, "estimated_days": 3},
            {"name": "Option 3", "type": "Pickup", "cost": 7, "estimated_days": 2},
            {"name": "Option 1", "type": "Delivery", "cost": 10, "estimated_days": 5},
        ]
        shippingOptions = ShippingOptions(input)
        output = shippingOptions.getSortedOptions()
        self.assertEqual(expected, output)

    def test_no_shipping_options_available(self):
        input = []
        expected = []
        shippingOptions = ShippingOptions(input)
        output = shippingOptions.getSortedOptions()
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
