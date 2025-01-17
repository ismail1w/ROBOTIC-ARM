#testing for our prediction
import cv2
import torch
import numpy as np

path='D:/govindarasan_ws/projects/02_tic_tac_toe/custom_object_detection_not_board/yolov5/best.pt'
model=torch.hub.load('ultralytics/yolov5','custom',path,force_reload=True)
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    results=model(frame)
    print(results.pred[0])
    frame=np.squeeze(results.render())
    cv2.imshow("FRAMES",frame)   
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()

