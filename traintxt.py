import numpy as np
import os
path = os.chdir("C:\\Users\\owuser\\Desktop\\新增資料夾\\change")
test = os.listdir(path)
print(test)
f = open("train.txt","w")
for i in range(len(test)):
    test[i] = test[i].replace('.txt',".jpg")
    txt = "/content/drive/My Drive/Colab Notebooks/darknet/data/obj/" + test[i] + '\n'
    print(txt)
    f.write(txt)

