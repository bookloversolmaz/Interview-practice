import detect_spikes
from detect_spikes import detect_spikes
def test_detect_spikes():
    data = [
        {"merchant_id": 101, "date": "2024-04-01", "amount": 100.0},
        {"merchant_id": 101, "date": "2024-04-02", "amount": 250.0},
        {"merchant_id": 101, "date": "2024-04-03", "amount": 120.0},
        {"merchant_id": 102, "date": "2024-04-01", "amount": 300.0},
        {"merchant_id": 102, "date": "2024-04-02", "amount": 600.0},
    ]

    expected = {
        101: ["2024-04-02"],
        102: ["2024-04-02"]
    }

    assert detect_spikes(data) == expected
