import json
from PIL import Image
import cv2
import numpy as np

def jsonreader(jsonpath, mode=1, convertRGB=True):
    """
    json파일을 해석해서 이미지와 함께 출력한다.
    jsonpath json파일의 위치를 입력한다.
    mode 
    1 = img, mask(2D, 0~1)를 함께 return한다. (array) 출력값 2개
    2 = img, mask(3D, 0~1)를 함께 return한다. (array) 출력값 2개
    3 = img, mask(2D, 0~255)를 함께 return한다. (array) 출력값 2개
    4 = img, mask(3D, 0~255)를 함께 return한다. (array) 출력값 2개
    5 = img를 cut하여 return한다. (array) 출력값 1개
    6 = img, mask를 함께 return한다. (image) 출력값 2개
    7 = img에 mask를 씌워서 return한다. (image) 출력값 1개
    8 = img를 cut하여 return한다. (image) 출력값 1개
    convertRGE
    True = RGB로 출력
    False = BGR로 출력
    """
    imgpath = jsonpath.replace('.json','').replace('labeling', 'train')
    with open(jsonpath) as read_json:
        jsonfile= eval(json.load(read_json))
    size = jsonfile['size']
    x0 = int(jsonfile['out_line']['x0'])
    x1 = int(jsonfile['out_line']['x1'])
    y0 = int(jsonfile['out_line']['y0'])
    y1 = int(jsonfile['out_line']['y1'])
    mask = np.zeros(size)
    mask[x0:x1,y0:y1] = 1
    img = cv2.imread(imgpath)
    if convertRGB: 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if mode == 1 :
        return img, mask

    elif mode == 2 :
        return img, np.dstack([mask, mask, mask])

    elif mode == 3 :
        return img, mask * 255

    elif mode == 4 :
        return img, np.dstack([mask, mask, mask]) * 255

    elif mode == 5 :
        return img[x0:x1,y0:y1]

    elif mode == 6 :
        return Image.fromarray((img).astype('u1')), Image.fromarray((255*mask).astype('u1'))

    elif mode == 7 :
        return Image.fromarray((img*np.dstack([mask, mask, mask])).astype('u1'))

    elif mode == 8 :
        return Image.fromarray((img[x0:x1,y0:y1]).astype('u1'))