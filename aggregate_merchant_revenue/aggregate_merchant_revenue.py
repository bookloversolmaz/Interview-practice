import math
from collections import defaultdict

def aggregate_merchant_revenue(records):
    """
    Aggregate revenue by merchant and category.

    Returns:
        Dict[int, Dict[str, float]]: merchant_id => category => total
    """
    # data is a list of dicts: got this right
    # Iterate over list using a for loop and organise dict by their merchant id in ascending order using sorted function, the 3rd key value pair
    # Use get method to organise by merchant ids
    # Then get the source for each dict under the merchant, find theses sources: card, cash and other
    # Under ech id use the get method to organise each source and add together the amounts. Use an if loop to do so.
    # Note that card sources are organised by card names, cash by cash and remainders are other
    # Return a new dict with each id representing a key and the value is another dict
    # organised by card, cash and other. Note that the amounts are whole numbers, so implementeither floor or ceil functions

    # result = {merchant: {"card": 0.0, "cash": 0.0, "other": 0.0}}: won't work as merchant is not yet defined. Need a dynamic 
    # Create a dict that initializes nested dicts automatically
    # If I try to access a merchant ID that doesn’t exist in the result dict yet, automatically create a value for that ID using this lambda function.”
    result = defaultdict(lambda: {"card": 0.0, "cash": 0.0, "other": 0.0})

    # Define known card sources
    card_sources = {"VISA", "MasterCard", "Amex"}
    
    for data in records:
        # merchant = data.get("merchant_id", 0).sort() can only call sort on lists
        merchant_id = data.get("merchant_id", 0)
        source = data.get("source", "")
        # amount is always the value
        # amount = data["amount"] use below version for safety and ensure whole numbers
        amount = math.floor(data.get("amount", 0.0))

        # if source in merchant["VISA"]: merchant is id, not a dict. "VISA" is a string; you're trying to do dictionary-style access on an int
        # first define card sources, then check if source is in there
        # if source in card_sources:
        # # result is a dictionary of merchants, so you need to access by merchant_id. You're updating a global "card", which doesn't exist in result.
        #     result["card"] += amount
        # elif source in merchant_id["Cash"]:
        #     result["cash"] += amount
        # else:
        #     result["other"] += amount
        
        # Classify source
        if source in card_sources:
            result[merchant_id]["card"] += amount
        elif source.lower() == "cash":
            result[merchant_id]["cash"] += amount
        else:
            result[merchant_id]["other"] += amount

    # Convert defaultdict back to regular dict for returning
    return dict(result)

    # TODO: Implement revenue aggregation logic
