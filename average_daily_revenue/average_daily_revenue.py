# def average_daily_revenue(records):
#     """
#     Calculates average daily revenue for each merchant.
    
#     Args:
#         records (List[Dict]): Each dict contains merchant_id, date, amount.
    
#     Returns:
#         Dict[int, float]: merchant_id -> average revenue per unique day
#     """
#     # TODO: Implement logic
#     return {}
# Aggregate the total revenue per day for each merchant
# Then calculate the average daily revenue for each merchant, based on the number of unique days

# Step 1: Describe the input and expected output types
# Step 2: Tell me how you’d group and aggregate the data before calculating averages
# data: input list of dicts. output a dict, where each key value pair are merchant_id(int) and average amount float
# define what to do: loop through the list of dicts and sort by merchant id. Organise this info in a new variable grouped = defaultdict() to take into account the fact that we don't know the number or name of the keys
# implement the action: now we need to find the daily average for each merchant id
# this involves loop through the grouped data. I do not know how many dates or the number of entries for each day are.
# so I need to organise the grouped data by date, and adding the amounts for the same date together
# so data is grouped = grouped by merchant id. Now grouped by merchant id and date[amounts]
# then keep a tally of the date for each merchant id merchant_days and add all of the amounts together to find the total_amount
# find the average by dividing total_mount / merchant_days
# process the result: return dict, the merchant id: average(float)

from collections import defaultdict

def average_daily_revenue(records):
    # initialise result dict to hold the final result. want a nested dict where the merchant id is followed by a dict that includes the date and amount. Need to group by merchant id and date
    # first group by merchant id, second group level by date followed by float for amount
    # defaultdict(float) → creates a dictionary where any missing key starts at 0.0
    # lambda: defaultdict(float) → this is a function that returns a defaultdict(float) whenever it's called
    # lambda is needed as defaultdict(...) expects a function, not a value. That function is called every time a missing key is accessed, and it returns the default value.
    grouped = defaultdict(lambda: defaultdict(float))
    averages = {}
    
    # loop over records and sort by merchant id, append new info to result dict
    for record in records:
        # As mentioned earlier, group by id, then date, then add amounts together
        merchant_id = record["merchant_id"]
        date = record["date"]
        amount = record["amount"]
        grouped[merchant_id][date] += amount
    # now grouped by id and date with amounts for each date added together
    # find the average by looping over grouped by looping over merchants and calculating average
    # grouped is a defaultdict where each value is another dictionary. That inner dictionary maps dates to daily revenue totals
    for merchant_id, amount in grouped.items():
        total_revenue = sum(amount.values())
        num_days = len(amount)
        # assigning the average daily revenue to this merchant in a new dictionary called averages.
        averages[merchant_id] = total_revenue / num_days
    return averages


