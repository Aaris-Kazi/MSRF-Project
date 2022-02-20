import cv2 as cv
import os
import pandas as pd
import matplotlib.pyplot as plt


img = cv.imread('images/00e77bde04dded4f9cc688a18d1f90c7ac4c2be4.tif')
# x = os.listdir('images/')
# df = pd.read_csv('lymph_dataset.csv')
# print(df[df.fi])
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
plt.imshow(hsv)
plt.show()
