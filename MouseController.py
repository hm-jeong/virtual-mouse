import autopy


class MouseController:
    def __init__(self):
        self.wScr, self.hScr = autopy.screen.size()
        print(f"screen size {self.wScr} {self.hScr}")

    def MoveCursor(self, dx, dy):
        curX, curY = autopy.mouse.location()
        # print(f"curX curY: {curX} {curY}")

        movX, movY = max(curX + dx, 0), max(curY + dy, 0)
        movX, movY = min(movX, self.wScr), min(movY, self.hScr)

        autopy.mouse.move(movX, movY)