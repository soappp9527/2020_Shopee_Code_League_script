import numpy as np
import pandas as pd

train_path = "../input/shopee-product-detection-open/train/train/train/"
test_path = "../input/shopee-product-detection-open/test/test/test/"
test_df = pd.read_csv("../input/shopee-product-detection-open/test.csv")

# prepare dataset
from tensorflow.keras.preprocessing.image import ImageDataGenerator

image_size = (224, 224)
batch_size = 128
seed = 9527

train_gen = ImageDataGenerator(rescale = 1/255, validation_split = 0.1)
train_set = train_gen.flow_from_directory(train_path, target_size = image_size, batch_size = batch_size, seed = seed, subset = "training")
val_set = train_gen.flow_from_directory(train_path, target_size = image_size, batch_size = batch_size, seed = seed, subset = "validation")

test_gen = ImageDataGenerator(rescale = 1/255)
test_set = train_gen.flow_from_dataframe(test_df, directory = test_path, target_size = image_size, batch_size = batch_size,
                                         seed = seed, shuffle = False, class_mode = None)#test dir have more files than test_df

#model buliding
from tensorflow.keras.applications import MobileNetV2
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

my_new_model = Sequential()
my_new_model.add(MobileNetV2(include_top = False, pooling = "avg", weights = "imagenet"))
my_new_model.add(Dense(42, activation = "softmax"))

my_new_model.layers[0].trainable = False# Indicate whether the first layer should be trained/changed or not.
my_new_model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])
my_new_model.summary()

#training
EPOCHS = 5
history = my_new_model.fit(train_set, epochs = EPOCHS, batch_size = batch_size, validation_data = val_set, shuffle = False)
my_new_model.save("model-MobileNetV2.hdf5")

#check
loss, acc = my_new_model.evaluate(val_set, batch_size = batch_size)
print("Validation acc (percent): %.2f" % (100 * acc))

#predict
prediton = my_new_model.predict(test_set, batch_size = batch_size)

test_df["category"] = prediton.argmax(axis = 1)
test_df["category"] = test_df["category"].apply(lambda x: str(x).zfill(2))# zero padding
test_df.to_csv("submission.csv", index = False)
