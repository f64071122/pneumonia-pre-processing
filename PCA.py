import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from cv2 import cv2 as cv2
import numpy as np
import os
os.chdir("C:\\Users\\owuser\\Desktop\\新增資料夾\\對比增強")
img = os.listdir("C:\\Users\\owuser\\Desktop\\新增資料夾\\對比增強")
for i in range(len(img)):
    photo = mpimg.imread(img[i])
    print(np.shape(photo))
    init = np.shape(photo)
    photo = photo[:,:,0]
    print(np.shape(photo))
    pca = PCA()
    pca.fit(photo)
    variances=pca.explained_variance_
    print(variances)
    thresh=0.8
    useful_features = variances > thresh
    num = np.sum(useful_features) # 計算True的個數
    new = PCA(n_components = num)
    ipca = new.fit(photo)
    print(new.explained_variance_ratio_)
    img_c = ipca.transform(photo)
    print(img_c.shape)
    temp = ipca.inverse_transform(img_c)
    temp = np.reshape(temp, (init[0],init[1]))
    plt.savefig("PCA_"+img[i])
    plt.show()
    #bug no picture
