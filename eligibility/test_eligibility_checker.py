from eligibility_checker import is_eligible


def test_valid_case():
    app = {
        "requested_amount": 20000,
        "business_start_date": "2022-01-01",
        "transaction_history": [
            {"month": "2023-04", "amount": 25000},
            {"month": "2023-05", "amount": 27000},
            {"month": "2023-06", "amount": 29000},
            {"month": "2023-07", "amount": 31000},
            {"month": "2023-08", "amount": 33000},
            {"month": "2023-09", "amount": 35000},
            {"month": "2023-10", "amount": 37000},
            {"month": "2023-11", "amount": 39000},
            {"month": "2023-12", "amount": 41000},
            {"month": "2024-01", "amount": 43000},
            {"month": "2024-02", "amount": 45000},
            {"month": "2024-03", "amount": 47000}
        ]
    }
    assert is_eligible(app) is True


def test_missing_months_allowed_for_low_value():
    app = {
        "requested_amount": 20000,
        "business_start_date": "2021-05-01",
        "transaction_history": [
            {"month": "2023-01", "amount": 25000},
            {"month": "2023-03", "amount": 26000},
            {"month": "2023-05", "amount": 27000},
        ]
    }
    assert is_eligible(app) is True


def test_high_value_with_missing_months_fails():
    app = {
        "requested_amount": 30000,
        "business_start_date": "2020-01-01",
        "transaction_history": [
            {"month": "2023-01", "amount": 31000},
            {"month": "2023-02", "amount": 32000},
            # missing months...
        ]
    }
    assert is_eligible(app) is False
