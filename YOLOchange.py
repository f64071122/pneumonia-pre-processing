#import pandas as pd
import numpy as np
import os
path = os.chdir("C:\\Users\\owuser\\Desktop\\新增資料夾\\Pneumonia Label")
GGO = os.listdir(path)
type(GGO) #list
GGO 
os.getcwd()
txtlen = []
txtcontent = []
#讀取GGO資料夾內的txt檔名
for file in GGO:
    content = open(file,"r")
    number = 0
    #用txtcontent儲存每個txt的每列內容
    for line in content.readlines():
        print(line)
        line = line.strip('\n')
        line = line.split(",")
        txtcontent.append(line)
        number +=1
    txtlen.append(number/2)  
    content.close() 
sum = 0
for i in range(len(txtlen)):
    sum += txtlen[i]
    sum = int(sum)

print("所有txt的內容列數/2:")
print(sum)
#合成大的txt 
txtcontent = np.array(txtcontent, dtype='float16')
#組成418*3的array
print(txtcontent)
print(np.shape(txtcontent))
#print(type(txtcontent))
label = []
for i in range(0, len(txtcontent) , 2):
    x = (txtcontent[i][0]+txtcontent[i+1][0])/2
    y = (txtcontent[i][1]+txtcontent[i+1][1])/2
    xl = (txtcontent[i+1][0]-txtcontent[i][0])
    yl = (txtcontent[i+1][1]-txtcontent[i][1])
    kind = txtcontent[i][2]
    label.append(kind)
    label.append(x)
    label.append(y)
    label.append(xl)
    label.append(yl)
print(np.shape(label))
print(len(label))    
#重組成(列數/2,5)的array
label = np.reshape(label, (sum, 5))
print(np.shape(label))
print(len(label))#要 = sum
print("over")
#label: 209*5, [種類 x中心 y中心 x邊長 y邊長]
#把一個txt的內容列數分出來
print(txtlen) #每一個txt有多少列/2，代表每一張照片有列數/2的bounding box
print(len(txtlen)) #有多少張照片
#要切割的份數必須是整數
txtlen[:] = [int(x) for x in txtlen]
print(txtlen)
print("over")
summ = 0
for i in range(len(txtlen)):
    summ +=txtlen[i]
    txtlen[i] = summ
print(txtlen)
label = np.vsplit(label,txtlen)
print(label[0])
print(label[1])
print(label[2])
print(len(label))#多一個，最後一列為解釋列，不需要
print("分割完成")
#label的每一個元素就是一個array，array的列數就是bounding box數
#先切出來再除長度
#取出每張圖片長度
from cv2 import cv2 as cv2
import csv
#讀取圖片名稱
os.chdir("C:\\Users\\owuser\\Desktop\\新增資料夾")
img = os.listdir("C:\\Users\\owuser\\Desktop\\新增資料夾\\Pne JPG")
print(img)
print(len(img)) #要等於label數量-1

for i in range(len(img)):
    name = cv2.imread("Pne JPG\\"+img[i])
    print(name)
    arr = label[i] 
    print("arr:")
    print(arr)
    print(name.shape[0]) #圖片高
    for j in range(len(arr)):
        arr[j][1] /= name.shape[1] #label第2行/寬度
        arr[j][2] /= name.shape[0] #label第3行/高度
        arr[j][3] /= name.shape[1] #label第4行/寬度
        arr[j][4] /= name.shape[0] #label第5行/高度
    #img抓出來的檔名.jpg要去掉 
    img[i] = img[i].replace('.jpg',".txt")
    np.savetxt(img[i],arr,fmt = '%5f',delimiter = ' ')
print("yolo only kind float")


