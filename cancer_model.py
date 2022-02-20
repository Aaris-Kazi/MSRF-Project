import os
from joblib import load
import cv2 as cv
import numpy as np

def can(img):
    rfc = load('multispec_rfc15.pickle')
    img = cv.imread('images/'+img)
    # img = cv.imread(img)
    pimg = np.array(img).flatten()
    p = rfc.predict([pimg])
    if p[0] == '1':
        x = 'Positive'
    else:
        x = 'Negative'
    # plt.imshow(img)
    # v = plt.show()
    return x
# plt.title(x)

x = os.listdir('images/')
for i in x:
    v= can(i)
    if v == 'Positive':
        print(i)

# 00e77bde04dded4f9cc688a18d1f90c7ac4c2be4.tif positive
# 00e77bde04dded4f9cc688a18d1f90c7ac4c2be4.tif positive