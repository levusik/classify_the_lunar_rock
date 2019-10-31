import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from keras.models import  load_model
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation, LeakyReLU
from keras.optimizers import Adam, RMSprop
from keras.callbacks import EarlyStopping, ReduceLROnPlateau

# load model
model = load_model('model.h5')
# summarize model.
model.summary()

dataset = os.path.join("Train Images", "Large")
files = os.listdir(os.path.join(dataset))

df = []
cnt = 0
for file in files[:40]:
    img = cv2.imread(os.path.join(dataset, file), cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (180, 120))
    #df.append( (file, np.round(model.predict(img.reshape(1, 180, 120, 3)) )))
    print(model.predict(img.reshape(1, 180, 120, 3)))


'''
d = {0 : "Small", 1: "Large"}
f = open("submission.csv", "w")
f.write("Image_File,Class\n")
for v in df:
    f.write(v[0] + "," + d[v[1][0][0]] + "\n")
f.close()
'''