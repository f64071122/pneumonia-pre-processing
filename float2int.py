#import pandas as pd
import numpy as np
import os
path = os.chdir("C:\\Users\\owuser\\Desktop\\新增資料夾\\change")
test = os.listdir(path)

for file in test:
    with open(file,'r+') as content:
        liness = []
        for line in content.readlines():
            
            if line[0:8] == "1.000000": 
                line = line.replace("1.000000","1")  
                liness.append(line)
                #print(liness)
            elif line[0:8] == "2.000000":
                line = line.replace("2.000000","2")
                liness.append(line)
                #print(liness)
            else:
                line = line.replace("3.000000","3")
                liness.append(line)
                #print(liness)
        content.seek(0)
        content.truncate()
        content.writelines(liness)
    content.close()


