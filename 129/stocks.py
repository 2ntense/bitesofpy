from collections import Counter, defaultdict

import requests

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == "n/a":
        return 0
    cap = cap.lstrip("$")
    if cap.endswith("M"):
        return float(cap.rstrip("M"))
    if cap.endswith("B"):
        return float(cap.rstrip("B")) * 1000
    return cap


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    total = 0
    for i in data:
        if i["industry"] == industry:
            total += _cap_str_to_mln_float(i["cap"])
    return round(total, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    top = ["", 0]
    for i in data:
        if _cap_str_to_mln_float(i["cap"]) > top[1]:
            top[0] = i["symbol"]
            top[1] = _cap_str_to_mln_float(i["cap"])
    return top[0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    d = defaultdict(float)
    for i in data:
        if i["sector"] == "n/a":
            continue
        d[i["sector"]] += _cap_str_to_mln_float(i["cap"])

    most = ["", 0]
    least = ["", float("inf")]

    for k, v in d.items():
        if v > most[1]:
            most[0] = k
            most[1] = v
        if v < least[1]:
            least[0] = k
            least[1] = v
    return most[0], least[0]
