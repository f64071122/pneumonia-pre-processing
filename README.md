# pneumonia-pre-processing
for project\
PCA.py 用於對照片進行PCA處理以增加training data的數量
\
comparison.py 用在對照片進行對比度、銳度、色度增強以增加training data的數量
\
enhancelabel.py 用在作出上面經過增強的training data的label data
\
float2int.py 用在將從YOLOchange.py作出的label data裡的種類資料從float轉換成int以符合yolov4的使用
\
PNG2JPG 用在將資料夾內所有的原始照片格式PNG轉成jpg以符合yolov4的使用並輸出
\
YOLOchange.py 用在將資料夾內所有的原始label data改成符合yolov4的label格式並輸出
\
traintxt.py 用於作出yolov4要求的train.txt(內含所有training data的路徑)
\
附上肺炎三個種類GGO、LLL、Pneumonia各一個的原始label、圖片和標籤說明
