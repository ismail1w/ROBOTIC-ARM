import cv2
import torch
import numpy as np
import time
import serial

path='D:/custom_object_detection_not_board/yolov5/best.pt'
model=torch.hub.load('ultralytics/yolov5','custom',path,force_reload=True)

# Define the serial port and baud rate
serial_port = "COM6"  # replace with your actual port
baud_rate = 9600  # replace with the baud rate used by your device

# Create a serial object
ser = serial.Serial(serial_port, baud_rate, timeout=1)

#defining string pattern
my_string="$EEEEEEEEE#"
print(my_string)
my_string_list=list(my_string)
print(my_string_list)

def myfunction(position,value): 
    my_string_list[position]=value
    my_string_new="".join(my_string_list)
    #print(my_string_new)
    my_string_new = my_string_new.encode('utf-8')
    ser.write(my_string_new)
    print(my_string_new)

# Open the serial port
if not ser.is_open:
    ser.open()

prediction_list=[]

color = (0, 255, 0)  # Green color in BGR
thickness = 2
#cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, thickness)
grid=[130,41,267,170,
      269,39,404,169,
      403,39,536,168,
      134,173,274,307,
      269,174,406,306,
      404,173,534,301,
      137,315,275,447,
      275,310,416,446,
      406,305,542,436]

def row_col_pos(predict):
    for i in range(0,len(predict)):
        #0,0
        if predict[i, 0]>=130 and predict[i, 1]>=41 and predict[i, 2]<= 267 and predict[i, 3]<=170:
            if int(predict[i, 5])==1:
                #tic_array[0,0]="O"
                #print("0,0='O'")
                #ser.write(b"$R0C0O#")
                myfunction(1,"O")
            elif int(predict[i, 5])==2:
                #tic_array[0,0]="X"
                #print("0,0='X'")
                myfunction(1,"X")
            else:
                myfunction(1,"E")
                
                
        #0,1
        if predict[i, 0]>=269 and predict[i, 1]>=39 and predict[i, 2]<= 404 and predict[i, 3]<=169:
            if int(predict[i, 5])==1:
                #tic_array[0,0]="O"
                #print("0,1='O'")
                myfunction(2,"O")
            elif int(predict[i, 5])==2:
                #tic_array[0,0]="X"
                #print("0,1='X'")
                myfunction(2,"X")
            else:
                myfunction(2,"E")
        
        #0,2
        if predict[i, 0]>=403 and predict[i, 1]>=39 and predict[i, 2]<= 536 and predict[i, 3]<=168:
            if int(predict[i, 5])==1:
                #tic_array[0,0]="O"
                #print("0,2='O'")
                myfunction(3,"O")
            elif int(predict[i, 5])==2:
                #tic_array[0,0]="X"
                #print("0,2='X'")
                myfunction(3,"X")
            else:
                myfunction(3,"E")
        #1,0
        if predict[i, 0]>=134 and predict[i, 1]>=173 and predict[i, 2]<= 274 and predict[i, 3]<=307:
            if int(predict[i, 5])==1:
                #tic_array[0,0]="O"
                #print("1,0='O'")
                myfunction(4,"O")
            elif int(predict[i, 5])==2:
                #tic_array[0,0]="X"
                #print("1,0='X'")
                myfunction(4,"X")
            else:
                myfunction(4,"E")
        #1,1
        if predict[i, 0]>=269 and predict[i, 1]>=174 and predict[i, 2]<= 406 and predict[i, 3]<=306:
            if int(predict[i, 5])==1:
                #tic_array[0,0]="O"
                #print("1,1='O'")
                myfunction(5,"O")
            elif int(predict[i, 5])==2:
                #tic_array[0,0]="X"
                #print("1,1='X'")
                myfunction(5,"X")
            else:
                myfunction(5,"E")
        #1,2
        if predict[i, 0]>=404 and predict[i, 1]>=173 and predict[i, 2]<= 534 and predict[i, 3]<=301:
            if int(predict[i, 5])==1:
                #tic_array[0,0]="O"
                #print("1,2='O'")
                myfunction(6,"O")
            elif int(predict[i, 5])==2:
                #tic_array[0,0]="X"
                #print("1,2='X'")
                myfunction(6,"X")
            else:
                myfunction(6,"E")
        #2,0
        if predict[i, 0]>=137 and predict[i, 1]>=315 and predict[i, 2]<= 275 and predict[i, 3]<=447:
            if int(predict[i, 5])==1:
                #tic_array[0,0]="O"
                #print("2,0='O'")
                myfunction(7,"O")
            elif int(predict[i, 5])==2:
                #tic_array[0,0]="X"
                myfunction(7,"X")
            else:
                myfunction(7,"E")
        #2,1
        if predict[i, 0]>=275 and predict[i, 1]>=310 and predict[i, 2]<= 416 and predict[i, 3]<=446:
            if int(predict[i, 5])==1:
                #tic_array[0,0]="O"
                #print("2,1='O'")
                myfunction(8,"O")
            elif int(predict[i, 5])==2:
                #tic_array[0,0]="X"
                #print("2,1='X'")
                myfunction(8,"X")
            else:
                myfunction(8,"E")
        #2,2
        if predict[i, 0]>=406 and predict[i, 1]>=305 and predict[i, 2]<= 542 and predict[i, 3]<=436:
            if int(predict[i, 5])==1:
                #tic_array[0,0]="O"
                #print("2,2='O'")
                myfunction(9,"O")
            elif int(predict[i, 5])==2:
                #tic_array[0,0]="X"
                #print("2,2='X'")
                myfunction(9,"X")
            else:
                myfunction(9,"E")
        
            

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    

    if not ret:
        print("Error reading frame from camera")
        break
    
    frame=cv2.resize(frame,(640,480))
    results=model(frame)
    #print(results.pred[0])
    prediction_tensor = results.pred[0]
    frame=np.squeeze(results.render())
    prediction_array = prediction_tensor.detach().cpu().numpy()
    #print(prediction_array)
    # Display the frame
    if results.pred[0] is not None and len(results.pred[0]) > 0:
        # Convert the tensor to a NumPy array
        prediction_array = results.pred[0].detach().cpu().numpy()

        # Extract individual elements
        #xmin = prediction_array[0, 0]
        #ymin = prediction_array[0, 1]
        #xmax = prediction_array[0, 2]
        #ymax = prediction_array[0, 3]
        #confidence = prediction_array[0, 4]
        #my_string="$EEEEEEEEE#"
        #my_string_list=list(my_string)
        for i in range(0,len(prediction_array)):
            class_label = int(prediction_array[i, 5])  # Assuming class label is an integer
            #print(f"class label: {class_label}")
        row_col_pos(prediction_array)
        #print(tic_array)
        # Print the extracted information
        #print(f"xmin: {xmin}")
        #print(f"ymin: {ymin}")
        #print(f"xmax: {xmax}")
        #print(f"ymax: {ymax}")
        #print(f"confidence: {confidence}")
        
        
    for i in range(0,36,4):
        #cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, thickness)
        cv2.rectangle(frame, (grid[i],grid[i+1]), (grid[i+2], grid[i+3]), color, thickness)
        
    cv2.imshow("USB Camera Feed", frame)
    time.sleep(0.4)

    # Break the loop if 'Esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

