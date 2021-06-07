import os 
import re
import cv2
import csv
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.preprocessing.image import ImageDataGenerator



def resize(raw_path=None, resize_path=None, height=128, width=128):
    file_list = os.listdir(raw_path)
    file_name = []
    for i in file_list:
        a = int(re.sub('[^0-9]', '', i))  
        file_name.append(a)

    for i, k in enumerate(file_list):
        img = cv2.imread(raw_path + '\\' + k)
        resize_img1 = cv2.resize(img, (height, width), interpolation=cv2.INTER_CUBIC)
        fix_img = cv2.cvtColor(resize_img1, cv2.COLOR_BGR2RGB) # 코드 추가 (색상 변형 문제 해결)
        x = str(file_name[i])
        cv2.imwrite(resize_path + "\\" + x + ".jpg", fix_img)     

    plt.imshow(fix_img)
    plt.show()  
    print("img shape", fix_img.shape)  
    


def image_load(path):
    file_list = os.listdir(path)
    
    file_name = []
    for i in file_list:
        a = int(re.sub('[^0-9]', '', i)) 
        
        file_name.append(a)
    file_name.sort()  
    
    file_res = []
    for j in file_name:
        file_res.append('%s\\%d.jpg' %(path,j) )
    
    image = []
    for k in file_res:
        img = cv2.imread(k)
        image.append(img)
    
    return np.array(image)



def csv_maker(path, k1=None, k2=None, k3=None, k4=None, k5=None):
    file = open(path, 'w')
    
    for i in range(k1):
        file.write(str(0) + '\n')
    for i in range(k2):
        file.write(str(1) + '\n')
    for i in range(k3):
        file.write(str(2) + '\n')
    for i in range(k4):
        file.write(str(3) + '\n')
    for i in range(k5):
        file.write(str(4) + '\n')        
    file.close

    

def label_load(path, label_cnt=None):

    file = open(path)
    labeldata = csv.reader(file)
    labellist = list(labeldata)
    label = np.array(labellist)
    label = label.astype(int)
    label = np.eye(label_cnt)[label]
    label = label.reshape(-1,label_cnt)
    return label



def next_batch( data1, data2, init, fina ):
    return data1[ init : fina ], data2[ init : fina ]



def shuffle_batch( data_list, label ) :
    x = np.arange( len( data_list) )
    random.shuffle(x)
    data_list2 = data_list[x]
    label2 = label[x]
    return data_list2,label2



# 이미지 증식 함수 추가
def datagen (path, data, count): # (경로, 데이터, 증식 횟수)

    X_datagen = ImageDataGenerator(horizontal_flip = False, # 수평 방향 뒤집기
                                   vertical_flip = False, # 수직 방향 뒤집기
                                   brightness_range = [0.1, 1.0], # 밝기 조절 범위
                                   zoom_range = 0.1, # 줌 범위
                                   width_shift_range = 0.2, # 수평 방향 이동
                                   height_shift_range = 0.2, # 수직 방향 이동
                                   rotation_range = 30, # 회전 각도 범위
                                   fill_mode = 'nearest' # 이미지를 회전, 이동, 축소할 때 생기는 공간을 채우는 방식
                                  )
    
    i = 0
    for batch in X_datagen.flow(data, batch_size=1,
                                save_to_dir=path, 
                                save_prefix='shoes', 
                                save_format='jpg'):
        i += 1
        if i > count:
            break  