import numpy as np
import cv2
#from LimitDetection import get_limits

#We used colorTracker.py to determine the Limit values for each color instead of get_limits() function.

red = [0, 0, 255] # BGR value of red
green = [0, 255, 0] # BGR value of green
blue = [255, 0, 0] # BGR value of blue
yellow = [0, 255, 255] # BGR value of yellow
cap = cv2.VideoCapture(0)

redLowerLimit = np.array([106, 157, 89])
redUpperLimit = np.array([179,255,255])

yellowLowerLimit = np.array([26, 113, 111])
yellowUpperLimit = np.array([179, 255, 255])

greenLowerLimit = np.array([66,155,40])
greenUpperLimit = np.array([98,255,255])

blueLowerLimit = np.array([88, 176, 70])
blueUpperLimit = np.array([133, 255, 255])

def yellow(img):
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvImage, yellowLowerLimit, yellowUpperLimit)
    _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for countour in contours:
        x = 600
        if cv2.contourArea(countour) > x:
            x,y,w,h = cv2.boundingRect(countour)
            cv2.rectangle(frame,(x,y), (x+w,y+h), color=(0,255,255), thickness=2)
            cv2.putText(frame, ("Detect"), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255),2)
            #print((x,y),(x+w,y+h))

def red(img):
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvImage, redLowerLimit, redUpperLimit)
    _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for countour in contours:
        x = 600
        if cv2.contourArea(countour) > x:
            x,y,w,h = cv2.boundingRect(countour)
            cv2.rectangle(frame,(x,y), (x+w,y+h), color=(0,0,255), thickness=2)
            cv2.putText(frame, ("Detect"), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255),2)
            #print((x,y),(x+w,y+h))

def green(img):
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvImage, greenLowerLimit, greenUpperLimit)
    _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for countour in contours:
        x = 600
        if cv2.contourArea(countour) > x:
            x,y,w,h = cv2.boundingRect(countour)
            x1 = int(x+x+w)//2
            y1 = int(y+y+h)//2
            cv2.circle(img,(x1,y1),4,(0,55,255),-1) #Showing center of the detected image
            cv2.rectangle(frame,(x,y), (x+w,y+h), color=(0,255,0), thickness=2)
            cv2.putText(frame, ("Detect"), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255),2)
            #print((x,y),(x+w,y+h))

def blue(img):
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvImage, blueLowerLimit, blueUpperLimit)
    _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for countour in contours:
        x = 600
        if cv2.contourArea(countour) > x:
            x,y,w,h = cv2.boundingRect(countour)
            cv2.rectangle(frame,(x,y), (x+w,y+h), color=(255,0,0), thickness=2)
            cv2.putText(frame, ("Detect"), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255),2)
            #print((x,y),(x+w,y+h))

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,480))  
    #yellow(frame)
    #green(frame)
    red(frame)
    blue(frame)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
       break