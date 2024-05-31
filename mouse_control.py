import autopy


class MouseController:
    def __init__(self):
        self.scr_width, self.scr_height = autopy.screen.size()
        print(f"screen size {self.scr_width} {self.scr_height}")

    def move_cursor(self, dx, dy):
        cur_x, cur_y = autopy.mouse.location()
        # print(f"curX curY: {curX} {curY}")

        dx, dy = max(cur_x + dx, 0), max(cur_y + dy, 0)
        dx, dy = min(dx, self.scr_width), min(dy, self.scr_height)

        autopy.mouse.move(dx, dy)