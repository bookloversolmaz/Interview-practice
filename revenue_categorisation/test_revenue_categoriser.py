from revenue_categoriser import categorize_transactions

def test_sample_input():
    txns = [
        {"type": "loan", "amount": 10000.00},
        {"type": "card", "amount": 2000.00},
        {"type": "refund", "amount": -300.00},
        {"type": "cash", "amount": 500.00},
        {"type": "loan", "amount": 2500.25},
        {"type": "card", "amount": 1500.50}
    ]
    result = categorize_transactions(txns)
    assert result == {
        "Loan Revenue": 12500.25,
        "Card Revenue": 3500.50,
        "Refund": -300.00,
        "Other": 500.00
    }

def test_empty_input():
    result = categorize_transactions([])
    assert result == {
        "Loan Revenue": 0.0,
        "Card Revenue": 0.0,
        "Refund": 0.0,
        "Other": 0.0
    }

def test_negative_card_amount_still_card():
    txns = [{"type": "card", "amount": -100.0}]
    result = categorize_transactions(txns)
    assert result["Card Revenue"] == -100.0
    assert result["Refund"] == 0.0  # because type matched before amount check
