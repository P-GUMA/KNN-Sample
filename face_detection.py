import numpy as np
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import glob
import os

#元画像を取り出して顔部分を正方形で囲み、64×64pにリサイズ、別のファイルにどんどん入れてく
in_dir = "./images/original/*.jpg"
out_dir = "./images/face"

# 画像ファイルの読み込み
in_jpg=glob.glob(in_dir)
# 元画像ファイル名を取得しておく
in_fileName=os.listdir("./images/original/")

for num in range(len(in_jpg)):
    image=cv2.imread(str(in_jpg[num]))
    
    # 画像データの読み込みに失敗した場合
    if image is None:
        print("Not open:",line)
        continue
    
    image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cascade = cv2.CascadeClassifier("./lbpcascade_animeface.xml")
    
    # 顔認識の実行
    face_list=cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=2,minSize=(64,64))
    #顔が１つ以上検出された時
    if len(face_list) > 0:
        for rect in face_list:
            x,y,width,height=rect
            image = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
            if image.shape[0]<64:
                continue
            image = cv2.resize(image,(64,64))
    
    #顔が検出されなかった時
    else:
        print("no face")
        continue
    
    #保存
    fileName=os.path.join(out_dir,str(in_fileName[num])+".jpg")
    cv2.imwrite(str(fileName),image)
