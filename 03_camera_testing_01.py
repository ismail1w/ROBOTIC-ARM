import cv2

# Define the rectangle parameters (top-left and bottom-right coordinates)
top_left = (50, 50)
bottom_right = (460, 460)
color = (255, 0, 0)  # Define color in BGR format (here, green: (0, 255, 0))
color1 = (0, 255, 0)  # Define color in BGR format (here, green: (0, 255, 0))
thickness = 2  # Thickness of the rectangle border (set to -1 for a filled rectangle)


def test_usb_camera():
    cap = cv2.VideoCapture(0)  # Initialize capturing video from the default camera (0)

    while True:
        ret, frame = cap.read()  # Read a frame from the camera

        # Display the captured frame in a window
        cv2.rectangle(frame, top_left, bottom_right, color, thickness)
        #draw sub rectangle
        cv2.rectangle(frame, (50,50), (50+136,50+136), color1, thickness)
        cv2.rectangle(frame, (50+136,50), (50+136+136,50+136), color1, thickness)
        cv2.rectangle(frame, (50+136+136,50), (50+136+136+136,50+136+136), color1, thickness)
        
        cv2.imshow('USB Camera Test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the video window
            break

    cap.release()
    cv2.destroyAllWindows()

# Start testing the USB camera
test_usb_camera()
q
