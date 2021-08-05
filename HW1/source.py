class Point:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.start = 0
        self.heuristic = 0
        self.end = 0

    def __eq__(self, other):
        return self.position == other.position


# please add your file in the same place oof source code

f = open('matrix.txt', 'r+')
playground = f.read()
f.close()

playground = playground.replace(" ", "")
arr = playground.split("\n")

comp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

xStart = 0
xEnd = 0
yStart = 0
yEnd = 0

# convert txt file into 2D array
for i in range(0, 10):
    for j in range(0, 10):
        if arr[i][j] == 'P':
            xStart = i
            yStart = j
            comp[i][j] = 0
        elif arr[i][j] == 'G':
            xEnd = i
            yEnd = j
            comp[i][j] = 0
        else:
            comp[i][j] = int(arr[i][j])


def aStarAlgorithm(pGround, start, end):

    startingPoint = Point(None, start)
    finishPoint = Point(None, end)

    startingPoint.start = startingPoint.heuristic = startingPoint.end = 0
    finishPoint.start = finishPoint.heuristic = finishPoint.end = 0

    openList = [startingPoint]
    closeList = []

    while len(openList) > 0:

        currentPoint = openList[0]
        currentPosition = 0
        k = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for index, item in enumerate(openList):
            if item.end < currentPoint.end:
                currentPoint = item
                currentPosition = index

        openList.pop(currentPosition)
        closeList.append(currentPoint)

        if currentPoint == finishPoint:
            path = []
            current = currentPoint

            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []

        for newPosition in k:

            pointPosition = (currentPoint.position[0] + newPosition[0], currentPoint.position[1] + newPosition[1])

            if pointPosition[0] > (len(pGround) - 1):
                continue

            if pointPosition[0] < 0:
                continue

            if pointPosition[1] > (len(pGround[len(pGround) - 1]) - 1):
                continue

            if pGround[pointPosition[0]][pointPosition[1]] != 0 or pointPosition[1] < 0:
                continue

            newPoint = Point(currentPoint, pointPosition)
            children.append(newPoint)

        for child in children:

            # delete repeated child
            for closed_child in closeList:
                if child == closed_child:
                    continue

            child.start = currentPoint.start + 1

            # heuristic is based on Pythagoras law for triangle
            pythagoras = ((child.position[0] - finishPoint.position[0]) ** 2) + (
                    (child.position[1] - finishPoint.position[1]) ** 2)

            child.heuristic = pythagoras
            child.end = child.start + child.heuristic

            # Child was in open list
            for open_node in openList:
                if child == open_node and child.start > open_node.start:
                    continue

            openList.append(child)


def main():
    board = comp

    start = (xStart, yStart)
    end = (xEnd, yEnd)

    path = aStarAlgorithm(board, start, end)
    print("Best path due to A* algorithm:")
    print(path)


if __name__ == '__main__':
    main()
