import cv2

# Replace with the IP address and port displayed in the IP Webcam app
url = "http://your_mobile_device_ip:8080/video"

# Open the video feed using OpenCV
cap = cv2.VideoCapture(url)

# Check if the video feed was opened successfully
if not cap.isOpened():
    print("Error opening video feed.")
    exit()

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Mobile Camera', frame)

    # Check if the user pressed the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
