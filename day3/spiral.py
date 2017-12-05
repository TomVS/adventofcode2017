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
'''

import math
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = int(f.read().strip())

    print "Input value:", data
    start = 1
    lower = int(math.floor(math.sqrt(data)))
    upper = lower+2

    i = 1
    while True:
        p = i**2
        if p < data:
            lower = p
        if p > data:
            upper = p
            break
        i += 2
        print i, "=>", p

    offset = data - (lower**2)
    joinMiddleSteps = math.floor(((offset+1)%lower)/2)
    print "offset", offset, (offset+1)%lower, joinMiddleSteps
    print "lower", lower
    print "Sum", lower + joinMiddleSteps - 1


if __name__ == '__main__':
    main()
