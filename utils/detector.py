from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image



def Get_detected_image(modelpth,img):
    model = YOLO(modelpth)
    results = model(img)

    id_name_dict = results[0].names
    cls_ids = results[0].boxes.cls
    ids = cls_ids.tolist()
    names = list(map(lambda x: id_name_dict[x], ids))

    bboxs = results[0].boxes.xyxy.cpu().numpy()
    detection = bboxs.astype(int)

    img = cv2.imread(img)
    for i in range(len(detection)):
        cv2.rectangle(img, (detection[i][0], detection[i][1]), (detection[i][2], detection[i][3]), (0, 255, 0), 2)
        #add labels
        cv2.putText(img, names[i], (detection[i][0], detection[i][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    
    img = Image.fromarray(img)
    return img