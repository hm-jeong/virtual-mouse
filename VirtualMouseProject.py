import math

import cv2
import numpy as np
from cv2 import Mat

import HandTrackingModule as htm
import time
import autopy
import pyautogui as pag

from Logger import log_message
from LogPlotter import LogPlotter


###################################
wCam, hCam = 1920, 1080
frameR = 100  # Frame Reduction
clocX, clocY = 0, 0
smoothening = 5
###################################

pTime = 0
scrollMode = 0
scrollLength = 0
pX, pY = 0, 0
click = 0

dataPath = 'C:/Users/lab/Desktop/연구/자료/data/video/'
filename = 'h_move_3.mov'
cap = cv2.VideoCapture(dataPath + filename)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
print(wScr, hScr)

prevImList = []


def calculateVectorMagnitude(im1, im2):
    return math.sqrt((im2[1] - im1[1]) ** 2 + (im2[0] - im1[0]) ** 2)


while True:
    # 1. Find hand landmarks
    success, img = cap.read()
    if not success:
        break

    draw_img = np.zeros_like(img)
    draw_img = detector.findHands(img, draw_img)
    ImList, bbox = detector.findPosition(img, draw_img)

    if len(prevImList) == len(ImList):
        for i in range(len(prevImList)):
            magnitude = calculateVectorMagnitude(prevImList[i], ImList[i])
            #print(i, magnitude)
            log_message("%d.log" % i, magnitude)

    prevImList = ImList

    # 2. Get the tip of the index finger
    # if len(ImList) != 0:
    # x1, y1 = ImList[8][1:]
    # x2, y2 = ImList[12][1:]
    # print(x1, y1, x2, y2)

    # 3. Check which fingers are up
    # fingers = detector.fingersUp()

    # 4. Only Index Finger : Moving Mode
    # if fingers[1] == 1 and fingers[2] == 0:
    #     length, img, lineInfo = detector.findDistance(8, 12, img)
    #
    #     # 5. Convert Coordinates
    #     cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
    #     x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
    #     y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))
    #     # 6. Smoothen Values
    #     clocX = plocX + (x3 - plocX) / smoothening
    #     clocY = plocY + (y3 - plocY) / smoothening
    #     # 7. Move Mouse
    #     autopy.mouse.move(wScr - clocX, clocY)
    #     cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
    #     plocX, plocY = clocX, clocY

    #8. Both Index and middle finger are up : Clicking Mode
    # if fingers[1] == 1 and fingers[2] == 1:
    #     # 9. Find distance between fingers
    #     length, img, lineInfo = detector.findDistance(8, 12, img)
    #     print(length)
    #
    #     # 10. Click mouse if distance short
    #     if length < 40:
    #         cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
    #         if click == 0:
    #             click = 1
    #             autopy.mouse.click()
    #     else:
    #         click = 0
    # else:
    #     click = 0

    # 13. Both Index and middle finger are up : Scrolling Mode
    # length, img, lineInfo = detector.findDistance(8, 12, img)
    #
    # if length < 40:
    #     cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
    #     if scrollMode == 0:
    #         scrollMode = 1
    #         print('start scroll mode')
    # else:
    #     if y2 - y1 > 10:
    #         pag.scroll(10)
    #         scrollMode = 0
    #         print('end scroll mode')
    #
    #     if y1 - y2 > 10:
    #         pag.scroll(-10)
    #         scrollMode = 0
    #         print('end scroll mode')

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(draw_img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    # 12. Display
    small_img = cv2.resize(img, (wCam // 3, hCam // 3))

    combined_img = draw_img.copy()
    combined_img[0: small_img.shape[0], -small_img.shape[1]:] = small_img

    cv2.imshow("Image", combined_img)
    cv2.waitKey(1)



log_file_paths = ['5.log', '6.log', '7.log', '8.log',
                  '9.log', '10.log', '11.log', '12.log',
                  '13.log', '14.log', '15.log', '16.log',
                  '17.log', '18.log', '19.log', '20.log']

plotter = LogPlotter(log_file_paths, dataPath)
plotter.plot_logs(filename.replace(".mov", ""))
