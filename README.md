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

### My strategy

NLP is not my area of interest, so I just skip it

---

## Week 5: [Logistics](https://www.kaggle.com/c/open-shopee-code-league-logistic)

### Task

Identify all the orders that are considered **late** depending on the **Service Level Agreements (SLA)**.

1. 1st attempt = 1st_deliver_attempt - pick, judge to be late if > SLA
2. 2nd attempt = 2nd_deliver_attempt - 1st_deliver_attempt, judge to be late if > 3 days regardless of origin to destination route
3. If no 2nd_deliver_attempt means 1st_deliver_attempt successful
4. All time formats are stored in epoch time based on Local Time (GMT+8)
5. Only consider the date when determining if the order is late; ignore the time
6. Only consider working days, excluding Sunday and public holidays (2020-03-08, 2020-03-25, 2020-03-30, 2020-03-31)
7. Both attempts need to be on time 

SLA matrix:

|   from_to    |  Metro Manila  |     Luzon      |    Visayas     |    Mindanao    |
| :----------: | :------------: | :------------: | :------------: | :------------: |
| Metro Manila | 3 working days | 5 working days | 7 working days | 7 working days |
|    Luzon     | 5 working days | 5 working days | 7 working days | 7 working days |
|   Visayas    | 7 working days | 7 working days | 7 working days | 7 working days |
|   Mindanao   | 7 working days | 7 working days | 7 working days | 7 working days |

### Data format

|  orderid   |    pick    | 1st_deliver_attempt | 2nd_deliver_attempt |                         buyeraddress                         |                        selleraddress                         |
| :--------: | :--------: | :-----------------: | :-----------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| 2215676524 | 1583138397 |     1583384958      |                     | Baging ldl BUENAVISTA,PATAG.CAGAYAN Buagsong,cordova,cebu Mt.VERNON Buolding, Habagat Lordman NATL Metro Manila | Pantranco vill. 417 Warehouse# katipunan 532 (UNIT Metro Manila |
| 2219624609 | 1583309968 |     1583463236      |     1583798576      | coloma's quzom CASANAS Site1 Masiyan 533A Stolberge 10,Baloy eastt away 041banahaw street,Tuguegarao agro, Metro Manila | BLDG 210A Moras C42B 2B16,168 church) Complex JUNKSHOP. 22-c Metro Manila |
| 2220979489 | 1583306434 |     1583459779      |                     | 21-O LumangDaan,Capitangan,Abucay,Bataan .Bignay Office,Buhanginan saBrgy186, 34i (bayanihan MALARIA, Alindahaw, Rm401, st.ngry p.pasubas metro manila |     #66 150-C, DRIVE, Milagros Joe socorro Metro Manila      |
| 2221066352 | 1583419016 |     1583556341      |                     | 616Espiritu MARTINVILLE,MANUYO #5paraiso kengi 12nn-9pm Brgy,Milagrosa 6Putohan,Tramo #18saint вєrnαвє st,CAA Metro Manila | 999maII 201,26 Villaruel Barretto gen.t number: 70-B 7A. MALL kanto- 1040 Metro Manila |
| 2222478803 | 1583318305 |     1583480500      |                     | L042 Summerbreezee1 L2(Balanay analyn Lot760 Cluster3-2T seppina UPPERG/L luzon | G66MANILA Hiyas Fitness MAYSILO magdiwang Lt.4C lot6 2F-48 st.,Binondo 1188Mall2M01 carnation Mae Metro Manila |

### Submission format

| **orderid** | **is_late** |
| :---------: | :---------: |
| 1955512445  |      0      |
| 1955598428  |      1      |

is_late: assign value 1 if the order is late, otherwise 0

### My strategy

1. Split location from address
2. Assign SLA by location
3. GMT+8 and transfer to date time
4. Working days count (np.busday_count)
5. Late judgement 

### Score

0.63885

Late Submission: 1.0

### Post-match review

1. Don't know how to count working days

2. Forget GMT+8

3. Need to use vectorization to speed up when deal with large dataset

---

## Week6:[Sentiment Analysis (Data Science)](https://www.kaggle.com/c/shopee-sentiment-analysis)

### Task

Build a customer review rating model

### Data format

| **review_id** |                          **review**                          | **rating** |
| :-----------: | :----------------------------------------------------------: | :--------: |
|     11576     | It's working properly. Very quick heating capability. Good product with this price thanks |     5      |
|     10293     | Excellent service by the staff, helpful and polite. Great experience overall. |     5      |
|     01820     | The delivery was fast but the packaging was not that good, the price is reasonable, overall the product is ok., |     4      |
|     32090     |                    Package not that well                     |     2      |

### Submission format

| review_id | rating |
| :-------: | :----: |
|   1156    |   1    |
|   2654    |   0    |

### My strategy

NLP is not my area of interest, so I just submit a table with all rating are 5

### Score

0.40517

---

## Week 7:[Short Algorithm Contest #2](https://www.hackerearth.com/challenges/competitive/shopee-programming-contest-2/?utm_campaign=Shopee+Programming+Contest+#2&utm_medium=email&utm_source=reminder-email)

### Task

Solve algorithm problems

### Score

10 (done by [mp0530](https://github.com/mp0530))

---

## Week 8: [Marketing Analytics](https://www.kaggle.com/c/open-shopee-code-league-marketing-analytics)

### Task

Predict whether users will open the marketing emails

### Data format

**[train/test].csv**

- `country_code`: An integer code for the country where the user lives.
- `grass_date`: The date when the email was sent.
- `user_id`: the unique identifier of each user
- `subject_line_length`: the number of characters in the subject of the email
- `last_open_day`: How many days ago was the last time the user opened an email
- `last_login_day`: How many days ago the user last logged in its Shopee account
- `last_checkout_day`: How many days ago the user last purchased on Shopee
- `open_count_last_[10/30/60]_days`: the total number of email opens in the last N days.
- `login_count_last_[10/30/60]_days`: the total number of user logins in the last N days.
- `checkout_count_last_[10/30/60]_days`: the total number of checkouts (=purchases) by the user in the last N days.
- `open_flag`: the target variable. Whether or not the email was opened.
- `row_id`:

**users.csv**
[empty values are simply unknown]

- `user_id`: the unique identifier of each user
- `attr_[1/2/3]`: general user attributes. Attr_1 and attr_2 are boolean, attrib_3 is categorical (can be integer [0,1,2,3,4])
- `age`: The user's reported age.
- `domain`: The user's top-level email domain. Less common domains are bundled together under the label 'other'.

### Submission format

| row_id | open_flag |
| :----: | :-------: |
|   0    |     1     |
|   1    |     1     |
|   2    |     0     |
|   3    |     0     |

### My strategy

1. EDA
2. data preprocess (data type, time code, date)
3. feature engineering (fill NA, remove outlier)
4. model selection (random forest, GBM, XGBoost, LightGBM)
5. grid search

my notebook

1. [EDA by R (data.table, ggplot2)](https://www.kaggle.com/soappp9527/marketing-analytics-eda-by-r-data-table-ggplot2)

2. [simple gbm model by h2o](https://www.kaggle.com/soappp9527/simple-gbm-model-by-h2o)

### Score

0.53353 (NO. 26)

### Post-match review

1. train and test dataset are not similar, so it's hard to find the right direction to improve accuracy
2. Lack of sensitivity for processing time series data, missing a lot of information
3. don't get right way to deal with NA
4. don't really understead the heperparameter in model, so can't grid search well
5. That's the best score of all shopee league competition, good job!

