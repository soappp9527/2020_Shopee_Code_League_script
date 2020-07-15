

# [2020 Shopee Code League](https://careers.shopee.sg/codeleague/?fbclid=IwAR0hnbAMRJdShIUVmL5LVhoy6OxXv6nE1jyW-Gn5_fpT9lOnIijorsbnVD8)
---
## Week 1: [Order Brushing](https://www.kaggle.com/c/order-brushing-shopee-code-league)

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

1. Use sliding window to  count  every shop-buyer transaction frequency by hour
2. Select the transaction frequency >= 3
3. Arrange userid by shopid

### Score

Out of time
Late Submission: 0.96712

### Post-match review

1. The use of pandas is not skilled enough
2. Didn't deal with time series data before
3. Running by my computer, computing power too low

---

## Week 2: [Product Detection](https://www.kaggle.com/c/shopee-product-detection-open)

### Task

Build a commodity **classification model** by ~100k images within 42 different categories.

### Data format

Images dataset

### Submission format

|               filename               | category |
| :----------------------------------: | :------: |
| fd663cf2b6e1d7b02938c6aaae0a32d2.jpg |    20    |
| c7fd77508a8c355eaab0d4e10efd6b15.jpg |    27    |
| 127f3e6d6e3491b2459812353f33a913.jpg |    04    |
| 5ca4f2da11eda083064e6c36f37eeb81.jpg |    22    |
| 46d681a542f2c71be017eef6aae23313.jpg |    12    |

### My strategy

Use pre-trained model from ImageNet (Transfer Learning)

### Score

0.67643

### Post-match review

1. Lack of relevant knowledge to build CNN model and adjust parameters by my own

2. Don't know how to enable GPU and TPU, so can only training with MobileNet which has minimal parameters

---

## Week 3: [Short Algorithm Contest #1](https://www.hackerearth.com/challenges/competitive/shopee-programming-contest-1/problems/)

### Task

Solve algorithm problems

### Score

Out of time

Too difficult to me  Q_Q

---

## Week 4: [Title Translation](https://www.kaggle.com/c/shopee-product-title-translation-open)

### Task

Translate product title in Traditional Chinese to English

###  Data format

|                        product_title                         |       category       |
| :----------------------------------------------------------: | :------------------: |
| Gucci Gucci Guilty Pour Femme Stud Edition 罪愛女性淡香水限量版 50ml T |   Health & Beauty    |
| （二手）PS4 GTA 5 俠盜獵車手5 Grand Theif Auto V繁體 中文版  |     Game Kingdom     |
|                            百獸卡                            | Life & Entertainment |
|                    nac nac活氧全效柔衣素                     |    Mother & Baby     |
| \#Nike耐吉官方F.C. 男子足球長褲新款標準型 拒水 拉鏈褲腳\nCD0557 |    Men's Apparel     |

### Submission format

### My strategy

### Score

### Post-match review

---

## Week 5: [Logistics](https://www.kaggle.com/c/open-shopee-code-league-logistic)

### Task

Identify all the orders that are considered late depending on the Service Level Agreements (SLA) with our Logistics Provider.



