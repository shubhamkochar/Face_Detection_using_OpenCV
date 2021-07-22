import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

cap = cv.VideoCapture(0)

ret, frame1 = cap.read()

cv.namedWindow("Threshold")

cv.createTrackbar("Threshold_lower","Threshold",100,255,nothing)


while cap.isOpened():
    ret, frame1 = cap.read()

    th_l = cv.getTrackbarPos("Threshold_lower","Threshold")
    

    gray = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
    # blur = cv.GaussianBlur(gray,(5,5),0)
    _, thresh = cv.threshold(gray,th_l,255,cv.THRESH_BINARY_INV)
    dilated = cv.dilate(thresh,None,iterations=3)
    contours,_ = cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(frame1,contours,-1,(0,0,255),2)

    for contour in contours:
        (x,y,w,h) = cv.boundingRect(contour)
        if cv.contourArea(contour) <1000:
            continue
        
        cv.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)

    cv.imshow("myCam",frame1)
    cv.imshow("thresh", thresh)

    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()
cap.release()

