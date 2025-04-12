from find_growth_streaks import find_growth_streaks
def test_find_growth_streaks():
    data = [
        {"merchant_id": 201, "date": "2024-04-01", "amount": 100.0},
        {"merchant_id": 201, "date": "2024-04-02", "amount": 120.0},
        {"merchant_id": 201, "date": "2024-04-03", "amount": 140.0},
        {"merchant_id": 201, "date": "2024-04-04", "amount": 80.0},
        {"merchant_id": 202, "date": "2024-04-01", "amount": 90.0},
        {"merchant_id": 202, "date": "2024-04-02", "amount": 95.0},
        {"merchant_id": 202, "date": "2024-04-03", "amount": 100.0},
        {"merchant_id": 202, "date": "2024-04-04", "amount": 110.0},
    ]

    expected = {
        201: ["2024-04-01", "2024-04-02", "2024-04-03"],
        202: ["2024-04-01", "2024-04-02", "2024-04-03", "2024-04-04"]
    }

    assert find_growth_streaks(data) == expected
