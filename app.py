import time
import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

enter = [0, 0, 0, 0, 0]
next = [1, 1, 0, 0, 0]
previous = [1, 0, 0, 0, 0]
close = [0, 0, 1, 1, 1]
shutdown = [1, 1, 1, 1, 1]
backspace = [0, 1, 1, 0, 0]
tasks = [0, 0, 0, 0, 1]


#camata setup 
cap = cv2.VideoCapture(0)
cap.set(3,1366)
cap.set(4,768)

#hand detector
detector = HandDetector(detectionCon=0.8,maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)   

    hands, img = detector.findHands(img)
    # print(img)
    # print(hands)
    if hands:
        hand=hands[0]
        fingers = detector.fingersUp(hand)
        
        #print(fingers)
        if(fingers == enter):
            print("Enter")
            pyautogui.press('enter')
        if(fingers == next):
            print("Next")
            pyautogui.press('right')
        if(fingers == previous):
            print("Previous")

            pyautogui.press('left')
        if(fingers == close):
            print("Close")
            #pyautogui.hotkey('alt', 'f4')
        if(fingers == shutdown):
            print("Shutdown")
            #os.system("shutdown /s /t 1") 
        if(fingers == backspace):
            print("Backspace")
            pyautogui.press("backspace")
        if(fingers == tasks):
            print("Tasks")
            pyautogui.keyDown('alt')
            pyautogui.keyDown('tab')
        time.sleep(1)   








    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break