import HandTrackingModule as htm
import CameraInputController as cic
import MouseController as mc

###################################
wCam, hCam = 640, 480


###################################

prevLmList = []


def getVariance(lmId):
    if len(lmList) == 0 or len(prevLmList) != len(lmList):
        return 0, 0

    prevX, prevY = prevLmList[lmId][1:]
    currX, currY = lmList[lmId][1:]
    return - (currX - prevX), currY - prevY


inputController = cic.CameraInputController(wCam, hCam)
detector = htm.HandDetector(maxHands=1)
mouseController = mc.MouseController()

while True:
    success, img, draw_img = inputController.readFrame()
    if not success:
        break

    # Find hand landmarks
    draw_img = detector.findHandLandmarks(img, draw_img, draw=True)
    lmList, bbox = detector.getLandmarksPosition(img, draw_img)

    dx, dy = getVariance(6)
    # print(f"dx dy: {dx} {dy}")
    mouseController.MoveCursor(dx, dy)

    prevLmList = lmList

    inputController.showFrame()
