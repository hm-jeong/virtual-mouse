import hand_detection as htm
import camera_control as cic
import mouse_control as mc

###################################
CAM_WIDTH, CAM_HEIGHT = 640, 480


###################################

lm_list, prev_lm_list = [], []


def _get_variance(lmId):
    if len(lm_list) == 0 or len(prev_lm_list) != len(lm_list):
        return 0, 0

    prev_x, prev_y = prev_lm_list[lmId][1:]
    curr_x, curr_y = lm_list[lmId][1:]
    return - (curr_x - prev_x), curr_y - prev_y


cam_input_controller = cic.CameraInputController(CAM_WIDTH, CAM_HEIGHT)
hand_detector = htm.HandDetector(maxHands=1)
mouse_controller = mc.MouseController()

while True:
    success, img, draw_img = cam_input_controller.readFrame()
    if not success:
        break

    # Find hand landmarks
    hand_detector.fine_hand_landmarks(img, draw_img, draw=True)
    lm_list = hand_detector.get_landmarks_position(img)

    dx, dy = _get_variance(6)
    # print(f"dx dy: {dx} {dy}")
    mouse_controller.move_cursor(dx, dy)

    prev_lm_list = lm_list

    cam_input_controller.show_frame()
