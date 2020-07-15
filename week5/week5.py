import numpy as np
import pandas as pd

data = pd.read_csv("../input/open-shopee-code-league-logistic/delivery_orders_march.csv")

#split address to location
data["buy"] = data["buyeraddress"].str.lower().str.split(" ").str[-1]
data["sell"] = data["selleraddress"].str.lower().str.split(" ").str[-1]

#count SLA day
def countday(df):
    if df["buy"] == "manila" and df["sell"] == "manila":
        return 3
    elif df["buy"] == "manila" and df["sell"] == "luzon":
        return 5
    elif df["buy"] == "luzon" and df["sell"] == "manila":
        return 5
    elif df["buy"] == "luzon" and df["sell"] == "luzon":
        return 5
    else:
        return 7

data["SLA"] = data.apply(countday, axis =1)

test = data.head(20)
test["2nd_deliver_attempt"].fillna(0, inplace = True)

#GMT+8
data[["pick", "1st_deliver_attempt", "2nd_deliver_attempt"]] += 8*60*60
#to date time
data["pick"] = pd.to_datetime(data["pick"],unit='s').dt.date
data["1st_deliver_attempt"] = pd.to_datetime(data["1st_deliver_attempt"],unit='s').dt.date
data["2nd_deliver_attempt"].fillna(0, inplace = True)#busday_count can't deal with na
data["2nd_deliver_attempt"] = pd.to_datetime(data["2nd_deliver_attempt"],unit='s').dt.date

#count workday
holidays = ["2020-03-08", "2020-03-25", "2020-03-30", "2020-03-31"]

data["frist_try"] = np.busday_count(data["pick"], data["1st_deliver_attempt"], weekmask="1111110", holidays = holidays)
data["second_try"] = np.busday_count(data["1st_deliver_attempt"], data["2nd_deliver_attempt"], weekmask="1111110", holidays = holidays)

def is_late(df):
    if df["frist_try"] > df["SLA"]:
        return 1
    else:
        if df["second_try"] > 3:
            return 1
        else:
            return 0        

data["is_late"] = data.apply(is_late, axis =1)

submission = data[["orderid", "is_late"]]
submission.to_csv("submission.csv", index = False)
