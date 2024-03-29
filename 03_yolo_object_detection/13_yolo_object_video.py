# 출처 : https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/
# 라이선스 : 학습으로만 사용.


import cv2, pafy
import numpy as np


# Load Yolo
net = cv2.dnn.readNet("./03_yolo_object_detection/yolov3.weights", "./03_yolo_object_detection/yolov3.cfg")
classes = []
with open("./03_yolo_object_detection/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))


# Loading video
#cap=cv2.VideoCapture(0) #내 pc 캠
url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)
best = video.getbest()
cap=cv2.VideoCapture(best.url) #비디오캡쳐 도구 사용


while(True):
    retval, img = cap.read()
    if not retval:
        break
    #img = cv2.imread("./data/girl.png")
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape


    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)


    net.setInput(blob)
    outs = net.forward(output_layers)


    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)


                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)


                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)


    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 2, color, 2)




    cv2.imshow("Image", img)
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
   
cv2.destroyAllWindows()