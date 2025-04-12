import unittest
from aggregate_merchant_revenue import aggregate_merchant_revenue

class TestMerchantAggregation(unittest.TestCase):
    def test_grouped(self):
        data = [
            {"amount": 100.0, "source": "VISA", "merchant_id": 101},
            {"amount": 40.0, "source": "Cash", "merchant_id": 101},
            {"amount": 70.0, "source": "PayPal", "merchant_id": 102},
        ]
        result = aggregate_merchant_revenue(data)
        expected = {
            101: {"card": 100.0, "cash": 40.0, "other": 0.0},
            102: {"card": 0.0, "cash": 0.0, "other": 70.0}
        }
        self.assertEqual(result, expected)
