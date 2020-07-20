import numpy as np
import os
from PIL import Image
os.chdir("C:\\Users\\owuser\\Desktop\\新增資料夾\\對比label")
dirname_read="C:\\Users\\owuser\\Desktop\\新增資料夾\\對比label"
dirname_write="C:\\Users\\owuser\\Desktop\\新增資料夾\\GGO enhance"
oldname=os.listdir(dirname_read)
#oldname_ch = os.listdir(dirname_read)
newnames=os.listdir(dirname_write)
print(oldname)
print(newnames)

for i in range(len(oldname)):
    newnames[i] = newnames[i].replace('.jpg','.txt')
    os.rename(oldname[i],newnames[i])