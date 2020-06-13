import pandas as pd
import numpy as np

data = pd.read_csv("data/Copy of Copy of order_brush_order.csv")
shop = pd.DataFrame(data["shopid"].unique(), columns=["shopid"])
#data[["day","time"]] = data["event_time"].str.split(expand=True)
#data["day"].unique()
data["event_time"] = pd.to_datetime(data["event_time"])
data_sort = data.set_index("event_time").sort_index()
data_silde = data_sort.groupby(["shopid", "userid"]).rolling("H").count()#sliding window

order_count = data_silde["orderid"].reset_index()
order_count = order_count.loc[order_count["orderid"]>=3]#filter

deal_count = order_count.groupby(["shopid","userid"]).size().reset_index()
deal_count["userid"] = deal_count["userid"].astype(str)

user_list = deal_count[["shopid","userid"]].groupby(["shopid"])["userid"].apply(lambda x: "&".join(x))#combine userid

final = pd.merge(shop,user_list, how = "left", on="shopid")
final = final.fillna(0)
final.to_csv("output/week1.csv", index=False)
