# def find_growth_streaks(records):
#     """
#     Finds the longest continuous growth streak for each merchant.
    
#     Args:
#         records (List[Dict]): Each record contains "merchant_id", "date", and "amount".
    
#     Returns:
#         Dict[int, List[str]]: merchant_id => list of date strings in the longest growth streak
#     """
#     # TODO: Implement growth streak logic
#     return {}

# get the data: data is a list of dicts containing 3 key value pairs of merchant id, date and amount. Output is a dict of keys that are merchant ids and the value is a list of dates in a string format
# define what to do: records are already organised by merchant id and date. I can iterate over the data and group by merchant id. use default dict as I don't know what the key/value will be, as this means that it can expand as needed
# then I can loop through the grouped records and compare the amount to the previous days amount. If there is any increase, I will add that to the result variable, that also uses default dic
# implement: implement using get method to organise the same merchant ids into one group. Then use for loop to iterate over grouped to compare previous and current amounts and track continous streaks, resetting when needed
# process result: return the result as a dict, so dict(result)

from collections import defaultdict
from datetime import datetime

def find_growth_streaks(records):
    grouped = defaultdict(list)
    longest_streak = defaultdict(list)
    current_streak = defaultdict(list)

    # 1. sort and organise by merchant id and date
    # group merchant id records together
    for record in records:
        grouped[record["merchant_id"]].append(record)
    
    # then sort each merchant id by date
    for merchant_id in grouped:
        grouped[merchant_id].sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
    
    # 2. Track, compare and update list of streaks
    # Tracks current_streak and longest_streak for each merchant 
    # Compares each day’s amount to the previous day. 
    # Updates the streak list accordingly
    # Loop through dates in grouped and compare the amount to previous days amount

    # track the longest streak
    # track the current streak
    # if amount in current streak is less than previous day, restart current streak
    # if at this point the current streak is longer than the longest, update longest streak

    # Process each merchant_id separately 
    # Loop through each merchant and their list of records
    # Compare amounts and track streaks
    for merchant_id, records in grouped.items():
        for i in range(len(records)):
            # Gets current date and amount
            date = records[i]["date"]
            amount = records[i]["amount"]
            
            # Represents the first day, as theres no previous day, start streak on that day
            if i == 0:
                current_streak[merchant_id] = [date]
            else:
            # Otherwise, compare this day to previous day
                prev_amount = records[i - 1]["amount"]
                
                if amount > prev_amount:
                    current_streak[merchant_id].append(date)
                else:
                    # otherwise the streak is broken. Was the streak I just had longer than the best one so far?
                    if len(current_streak[merchant_id]) > len(longest_streak[merchant_id]):
                        # If yes → save it as the new best:
                        longest_streak[merchant_id] = current_streak[merchant_id]
                    # Then reset the streak and startover from this date.
                    current_streak[merchant_id] = [date]
        # ecause the streak might still be going at the very end of the data, and we need to compare one last time to make sure we didn’t miss a record-breaking run.
        if len(current_streak[merchant_id]) > len(longest_streak[merchant_id]):
            longest_streak[merchant_id] = current_streak[merchant_id]

    return dict(longest_streak)