# It is my competition script of [2020 Shopee Code League](https://careers.shopee.sg/codeleague/?fbclid=IwAR0hnbAMRJdShIUVmL5LVhoy6OxXv6nE1jyW-Gn5_fpT9lOnIijorsbnVD8)

[TOC]

## Week1: [Order Brushing](https://www.kaggle.com/c/order-brushing-shopee-code-league)

---

### Task

Identify all shops and buyers that are deemed to have conducted order brushing by **concentrate rate** is greater than or equal to 3 at any instance.

```
Concentrate rate = 
Number of Orders within 1 hour / Number of Unique Buyers within 1 hour
```

### Data format

|    orderid     |  shopid  |  userid  |     event_time      |
| :------------: | :------: | :------: | :-----------------: |
| 31076582227611 | 93950878 | 30530270 | 2019-12-27 00:23:03 |

### Submission format

|  shopid   |      userid       |
| :-------: | :---------------: |
| 162014252 |     183926374     |
| 321014322 | 19233237&23421231 |
| 22754767  |         0         |

### My strategy

1. use sliding window to  count  every shop-buyer transaction frequency by hour
2. select the transaction frequency >= 3
3. arrange userid by shopid

### Score

out of time
Late Submission: 0.96712

### Post-match review

1. the use of pandas is not skilled enough
2. didn't deal with time series data before
3. running by my computer, computing power too low