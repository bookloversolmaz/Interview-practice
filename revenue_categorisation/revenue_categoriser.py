from typing import List, Dict
# You're working on Liberis’ internal finance data processing tool. Task is to:
# 1. Categorize each transaction based on its type and amount
# 2. Return the total amount per revenue category, rounded to 2 decimal places

# TO DO
# 1. Get the data:
# Provided data in the test
# 2. Define what to do
# Format the data:
# Iterate over list and collect each type together, ordering each into sequence below
# Take the second key/value in each dict and add the values for each type together. Can see from test that the program does not do this
# 3. Implement the action
# After interating, add each value of every data type into four results rounded to 2 decimal places:
# Loan Revenue:, Card Revenue:, Refund: -, Other:
# 4. Process the result
# The result should be in a dictionary where each data type is a separate key value pair
def categorize_transactions(transactions: List[Dict]) -> Dict[str, float]:
    # TODO: Implement logic here
    result = {
        "Loan Revenue": 0.0,
        "Card Revenue": 0.0,
        "Refund": 0.0,
        "Other": 0.0
    }
    for txn in transactions:
        t_type = txn.get("type", "")
        amount = txn.get("amount", 0.0)

        if t_type == "loan":
            result["Loan Revenue"] += amount
        elif t_type == "card":
            result["Card Revenue"] += amount
        elif amount < 0:
            result["Refund"] += amount
        else:
            result["Other"] += amount

    # Optional: Round everything to 2 decimal places
    # Loops through all the keys in the result dictionary 
    # result[category]
    # Retrieves the total amount (float) associated with that category.
    for category in result:
        result[category] = round(result[category], 2)
    return result
    # return {
    #     "Loan Revenue": 0.0,
    #     "Card Revenue": 0.0,
    #     "Refund": 0.0,
    #     "Other": 0.0
    # }
# Test results:
# Sample input: does not ouput info in correct format, assertion error
# Negative card amount: 