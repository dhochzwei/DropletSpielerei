"""
Simple script to test video capture capabilities
"""
import numpy as np
import cv2

# get video device
cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # create grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # now do something, for example run the Canny-Edge-Detector
    canny = cv2.Canny(gray,50,100)
    # Display the resulting frame
    cv2.imshow('frame',canny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()