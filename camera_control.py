import cv2
import numpy as np
import time


class CameraInputController:
    def __init__(self, w, h):
        self.camera = cv2.VideoCapture(0)
        self.pTime = 0
        self.w, self.h = w, h

    def readFrame(self):
        result, self.img = self.camera.read()
        if result is not True:
            print('Failed to read frame')
            return result

        self.draw_img = np.zeros_like(self.img)
        return result, self.img, self.draw_img

    def show_frame(self):
        # Frame Rate
        cTime = time.time()
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime
        cv2.putText(self.draw_img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Display
        small_img = cv2.resize(self.img, (self.w // 3, self.h // 3))

        combined_img = self.draw_img.copy()
        combined_img[0: small_img.shape[0], -small_img.shape[1]:] = small_img

        cv2.imshow("Image", combined_img)
        cv2.waitKey(1)