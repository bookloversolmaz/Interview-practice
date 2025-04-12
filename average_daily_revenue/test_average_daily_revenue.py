from average_daily_revenue import average_daily_revenue
def test_average_daily_revenue():
    data = [
        {"merchant_id": 301, "date": "2024-04-01", "amount": 100.0},
        {"merchant_id": 301, "date": "2024-04-01", "amount": 50.0},
        {"merchant_id": 301, "date": "2024-04-02", "amount": 200.0},
        {"merchant_id": 302, "date": "2024-04-01", "amount": 300.0},
        {"merchant_id": 302, "date": "2024-04-03", "amount": 300.0},
    ]
    expected = {
        301: 175.0,
        302: 300.0
    }
    assert average_daily_revenue(data) == expected
