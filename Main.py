import API
import collections

from Direction import Direction
from Maze import Maze
from Mouse import Mouse


def main():
    maze = Maze(API.mazeWidth(), API.mazeHeight())
    mouse = Mouse(0, 0, Direction.NORTH)
    while not maze.inCenter(mouse.getPosition()):
        updateWalls(maze, mouse)
        moveOneCell(maze, mouse)


def updateWalls(maze, mouse):
    position = mouse.getPosition()
    direction = mouse.getDirection()
    if API.wallFront():
        maze.setWall(position, direction)
    if API.wallLeft():
        maze.setWall(position, direction.turnLeft())
    if API.wallRight():
        maze.setWall(position, direction.turnRight())


def moveOneCell(maze, mouse):
    # Compute the next direction
    currentX, currentY = mouse.getPosition()
    nextX, nextY = getNextCell(maze, mouse)
    if nextX < currentX:
        nextDirection = Direction.WEST
    if nextY < currentY:
        nextDirection = Direction.SOUTH
    if nextX > currentX:
        nextDirection = Direction.EAST
    if nextY > currentY:
        nextDirection = Direction.NORTH

    # Turn and move to the next cell
    currentDirection = mouse.getDirection()
    if currentDirection.turnLeft() == nextDirection:
        mouse.turnLeft()
    elif currentDirection.turnRight() == nextDirection:
        mouse.turnRight()
    elif currentDirection != nextDirection:
        mouse.turnAround()
    mouse.moveForward()


def getNextCell(maze, mouse):
    initial = mouse.getPosition()
    center = None
    ancestors = {}
    queue = collections.deque([initial])
    while queue:
        current = queue.popleft()
        for direction in Direction:
            neighbor = getNeighbor(current, direction)
            # If the neighbor is out of bounds, skip
            if not maze.contains(neighbor):
                continue
            # If the neighbor is blocked by wall, skip
            if maze.getWall(current, direction):
                continue
            # If the neighbor is already discovered, skip
            if neighbor in ancestors:
                continue
            # Add the neighbor to queue and update ancestors
            queue.append(neighbor)
            ancestors[neighbor] = current
            if maze.inCenter(neighbor):
                center = neighbor
        # If a center cell was found, stop searching
        if center:
            break

    # Walk backwards from the center
    position = center
    while ancestors[position] != initial:
        position = ancestors[position]
    return position


def getNeighbor(current, direction):
    x, y = current
    if direction == Direction.NORTH:
        y += 1
    if direction == Direction.EAST:
        x += 1
    if direction == Direction.SOUTH:
        y -= 1
    if direction == Direction.WEST:
        x -= 1
    return (x, y)


if __name__ == "__main__":
    main()
