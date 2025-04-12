# def detect_spikes(records):
    # Detects spike days where a merchant had 2x or more revenue than the day before.
    
    # Args:
    #     records (List[Dict]): Each record contains "merchant_id", "date", and "amount".
        
    # Returns:
    #     Dict[int, List[str]]: merchant_id -> list of spike dates
    # """
    # # TODO: Implement spike detection logic
    # # return {}

# The key is the merchant ID
# The value is a list of dates where a spike occurred (compared to the previous day for that merchant

# returns
# {
#     101: ["2024-04-02"],
#     102: ["2024-04-02"]
# }

# Logic:
# Get the data: the data is a list of dicts, the output is a dict where the key is the merchant_id which is an int, and the value is a list containing the data as a string
# Define what to do: firstly, I need to aggregate each of the same merchant_ids so that I can then successfully compare the dates and the amounts to find if a particualr date has at least twice the amount as the previous date.
# To do that, I need to first store the aggregated data. result = (merchant_id: [date]). I don't know what the merchant id is or how many there are.

# My attempt
# I will use a defaultdict, as I don't know what the key value in the result dict will be. So, result = defaultdict(list), and I will use list as I also don't know how many datetime values I will need.
# I will get the merchant_ids by using a for loop and then aggregating the merchant ids using the get method. So, for data in records: results["merchant_id"].append(data)
# I will then sort the merchant ids by date. Dates in python fall under datetime, so import datetime at the top
# I want to create a new list of dates, so I will used sorted function. results(sorted["date"]).append(data)
# I will then compare the amount to the previous days amount. I will use an if loop. if current date is at least twice the previous days amount, I will keep that date, otherwise I will remove it from results
# if amount in date >= 2 * amount of previous day, leave result, else .remove(dict)

# ChatGPT's fix
# for data in records: results["merchant_id"].append(data) WRONG! Should be:
# for record in records:
    # grouped[record["merchant_id"]].append(record) 
# "merchant_id" should not be quoted here (you want the value, not the literal string)
# grouped is the right variable name for this intermediate step
# results(sorted["date"]).append(data) WRONG
# for merchant_id in grouped:
    # grouped[merchant_id].sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
# You sort in place using .sort() on the list of records
# datetime.strptime() parses the string date into a datetime object so it can be sorted chronologically
# if amount in date >= 2 * amount of previous day wrong and unclear!
    # for i in range(1, len(grouped[merchant_id])):
    # prev = grouped[merchant_id][i - 1]["amount"]
    # curr = grouped[merchant_id][i]["amount"]
    # if curr >= 2 * prev:
    #     spikes[merchant_id].append(grouped[merchant_id][i]["date"])
# Use for loop to iterate over grouped. If crr is twice that of previous day, add to result

from datetime import datetime
from collections import defaultdict

def detect_spikes(records):
    # Each key is a merchant ID, Each value is a list of revenue records (dictionaries)
    grouped = defaultdict(list)
    spikes = defaultdict(list)

    # 1. group all records
    for record in records:
        # Append to grouped list each record by merchant id
        # record["merchant_id"] finds the merchant ids in records
        # "Go to the list of records for merchant 101, and add this record to it."
        grouped[record["merchant_id"]].append(record)

    # 2. Sort each merchant id by date   
        # Loop over each merchant id within grouped to organise by date, using strptime to convert string into datetime object to sort by date
        # use sort to sort group in place, the key or sorting criteria is a function named lambda x, that sorts by date
        # Sorts merchant ids by date
    for merchant_id in grouped:
        # "Sort the list of records for this merchant by date, from oldest to newest, using proper date parsing."
        grouped[merchant_id].sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))

    # 3. Loop through sorted list and detect spikes
        # Another for loop using range, which returns a sequence of numbers starting from 1 and organised by the length of the merchant_ids in grouped
        # sorts merchant ids by length
        for i in range(1, len(grouped[merchant_id])):
        # compares the dates. Previous is the previous date in the same merchant id, curr is current
            prev = grouped[merchant_id][i - 1]["amount"]
            curr = grouped[merchant_id][i]["amount"]
            if curr >= 2 * prev:
            # create new variable to hold spike dates by merchant id
                spikes[merchant_id].append(grouped[merchant_id][i]["date"])

   
    return dict(spikes)

