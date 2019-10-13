import API

from Direction import Direction


class Mouse:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def getPosition(self):
        return (self.x, self.y)

    def getDirection(self):
        return self.d

    def turnLeft(self):
        API.turnLeft()
        self.d = self.d.turnLeft()

    def turnRight(self):
        API.turnRight()
        self.d = self.d.turnRight()

    def turnAround(self):
        self.turnRight()
        self.turnRight()

    def moveForward(self):
        API.moveForward()
        if self.d == Direction.NORTH:
            self.y += 1
        if self.d == Direction.EAST:
            self.x += 1
        if self.d == Direction.SOUTH:
            self.y -= 1
        if self.d == Direction.WEST:
            self.x -= 1
