import cv2
import torch
import numpy as np

path = 'D:/govindarasan_ws/projects/02_tic_tac_toe/custom_object_detection_not_board/yolov5/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)

# USB camera reading
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    # Get prediction results
    results = model(frame)
    pred = results.pred[0]

    for det in pred:
        # Extract bounding box coordinates
        xmin, ymin, xmax, ymax = int(det[0]), int(det[1]), int(det[2]), int(det[3])

        # Draw bounding box on the frame
        color = (0, 255, 0)  # Green color in BGR
        thickness = 2
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, thickness)

        # Print bounding box coordinates
        print(f"Object detected at: ({xmin}, {ymin}) - ({xmax}, {ymax})")

    cv2.imshow("FRAMES", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
