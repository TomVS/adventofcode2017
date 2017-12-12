'''
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a
location marked 1 and then counting up while spiraling outward.
For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested
data must be carried back to square 1 (the location of the only access
port for this memory system) by programs that can only move up, down,
left, or right. They always take the shortest path: the Manhattan Distance
between the location of the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified
in your puzzle input all the way to the access port?

Your puzzle input is 265149.

--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?

Your puzzle input is still 265149.
'''

import math
import sys

def spiralDist(data):

    print "Input value:", data

    if data == 1:
        print "Special case: 1"
        return 0

    lower = 1
    upper = 3
    level = 0

    # Find the lower and upper level bounds
    i = 1
    while True:
        p = i**2
        if p >= data:
            upper = i
            lower = i-2
            break
        i += 2
        level += 1

    print "lower", lower, "upper", upper, "level", level
    offset = data - (lower**2)
    print "offset", offset
    modulo = upper-1
    adjOffset = ((offset)%modulo) - level
    print "new", (offset)%modulo, '-', level , '=', adjOffset
    joinMiddleSteps = abs(adjOffset)
    joinCentreSteps = level
    print "steps to middle of side", joinMiddleSteps
    print "steps to centre from middle", joinCentreSteps
    print "Sum", joinCentreSteps + joinMiddleSteps


def spiralSum(data):
    size = int(math.ceil(math.sqrt(data)))

    startx = size/2
    starty = size/2

    print data, size, startx, starty

    matrix = [[0 for i in range(size)] for j in range(size)]

    firstBiggestSum = 0
    localSum = 0

    x = startx
    y = starty
    dirs = [(0,1),(-1,0),(0,-1),(1,0)]
    neighbours = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    curDirIdx = 0 # start by going right
    for n in range(data):
        # Now add sum of cells around
        if n == 0:
            matrix[x][y] = 1
        else:
            localSum = 0
            for i, xy in enumerate(neighbours):
                nx, ny = xy
                if x+nx < 0 or x+nx >= size:
                    continue
                if y+ny < 0 or y+ny >= size:
                    continue
                localSum += matrix[x+nx][y+ny]
                # print nx, ny, matrix[x+nx][y+ny], "#", localSum
            matrix[x][y] = localSum

        potentialNewDir = dirs[(curDirIdx +1)%4]
        if matrix[x+potentialNewDir[0]][y+potentialNewDir[1]] == 0:
            curDirIdx = (curDirIdx +1)%4

        if matrix[x][y] > data:
            print "The next biggest value after", data, "is", matrix[x][y]
            return

        x += dirs[curDirIdx ][0]
        y += dirs[curDirIdx ][1]


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = int(f.read().strip())

    spiralDist(data)
    print "================"
    spiralSum(data)

    # for i in range(1020, 1025):
    #     print "======================================="
    #     spiralDist(i)


if __name__ == '__main__':
    main()
