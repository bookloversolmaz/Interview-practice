from datetime import datetime
from typing import Dict, List


def is_eligible(application: Dict) -> bool:
    """
    Determine if a business is eligible for a Business Cash Advance (BCA) loan.
    """
    # Step 1: Validate requested amount
    amount = application.get("requested_amount")
    if not (5000 <= amount <= 50000):
        return False

    # Step 2: Validate business age
    start_date = datetime.strptime(application["business_start_date"], "%Y-%m-%d")
    if (datetime.today() - start_date).days < 365:
        return False

    # Step 3: Prepare transaction history
    transactions = {t["month"]: t["amount"] for t in application["transaction_history"]}
    current_year = datetime.today().year
    current_month = datetime.today().month
    last_12_months = []

    for i in range(12):
        m = (current_month - i - 1) % 12 + 1
        y = current_year - ((i + 1 - current_month) // 12)
        last_12_months.append(f"{y:04d}-{m:02d}")

    # Step 4: High value rule check
    high_value = amount > 25000
    month_values = []

    for month in last_12_months:
        if month in transactions:
            month_values.append(transactions[month])
        else:
            if high_value:
                return False  # no missing months allowed
            else:
                continue  # fill with average later

    if not month_values:
        return False

    average = sum(month_values) / len(month_values)
    filled_month_values = [transactions.get(m, average) for m in last_12_months]

    # Step 5: Check all monthly values > requested amount
    return all(m > amount for m in filled_month_values)
