from PIL import Image,ImageEnhance
import numpy as np
from cv2 import cv2 as cv2
import numpy as np
import os
os.chdir("C:\\Users\\owuser\\Desktop\\新增資料夾\\對比增強")
img = os.listdir("C:\\Users\\owuser\\Desktop\\新增資料夾\\對比增強")

for i in range(len(img)):
    photo = Image.open(img[i])
    enh = ImageEnhance.Contrast(photo)
    contrast = 5
    enh = enh.enhance(contrast)
    #enh = ImageEnhance.Color(photo)
    #color = 5
    #enh = enh.enhance(color)
    enh = ImageEnhance.Sharpness(enh)
    sharpness = 10
    enh = enh.enhance(sharpness)
    enh.save("_enh4"+img[i])