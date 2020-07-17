import numpy as np
import pandas as pd

data = pd.read_csv("../input/open-shopee-code-league-logistic/delivery_orders_march.csv")
#split address to location
data["buy"] = data["buyeraddress"].apply(lambda x: x.split(" ")[-1].lower())
data["sell"] = data["selleraddress"].apply(lambda x: x.split(" ")[-1].lower())

#count SLA day
SLA = pd.DataFrame(
    data = [
            ["manila","manila",3],
            ["manila","luzon",5],
            ["manila","visayas",7],
            ["manila","mindanao",7],
            ["luzon","manila",5],
            ["luzon","luzon",5],
            ["luzon","visayas",7],
            ["luzon","mindanao",7],
            ["visayas","manila",7],
            ["visayas","luzon",7],
            ["visayas","visayas",7],
            ["visayas","mindanao",7],
            ["mindanao","manila",7],
            ["mindanao","luzon",7],
            ["mindanao","visayas",7],
            ["mindanao","mindanao",7]
           ],
    columns=["buy", "sell", "SLA"]
)

data = pd.merge(data, SLA, on = ["buy", "sell"])

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

#judge
data["is_late"] = (data["frist_try"] > data["SLA"]) | (data["second_try"] > 3)
data["is_late"] = data["is_late"].astype(int)

submission = data[["orderid","is_late"]]
submission.to_csv("submission.csv", index = False)
