#testing for our prediction
import cv2
import torch
import numpy as np

path='D:/govindarasan_ws/projects/02_tic_tac_toe/custom_object_detection_not_board/yolov5/best.pt'
model=torch.hub.load('ultralytics/yolov5','custom',path,force_reload=True)
'''
#rectangle boxes
top_left = (50, 50)
bottom_right = (300, 300)
color = (0, 255, 0)  # Define color in BGR format (here, green: (0, 255, 0))
thickness = 2  # Thickness of the rectangle border (set to -1 for a filled rectangle)
'''
#usb camera reading
cap=cv2.VideoCapture(0)


while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    results=model(frame)
    print(results.pred[0])
    frame=np.squeeze(results.render())
    
    #draw rectangle for images
    #cv2.rectangle(frame, top_left, bottom_right, color, thickness)
    cv2.imshow("FRAMES",frame)   
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()


