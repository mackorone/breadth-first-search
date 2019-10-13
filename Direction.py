import enum


class Direction(enum.Enum):
    NORTH = "n"
    EAST = "e"
    SOUTH = "s"
    WEST = "w"

    def turnLeft(self):
        return {
            Direction.NORTH: Direction.WEST,
            Direction.EAST: Direction.NORTH,
            Direction.SOUTH: Direction.EAST,
            Direction.WEST: Direction.SOUTH,
        }[self]

    def turnRight(self):
        return {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }[self]
