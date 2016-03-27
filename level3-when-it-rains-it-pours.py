# Author: Terri Wong <terriwmj@gmail.com>

"""
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held, but a sudden storm puts your escape plans at risk. The structural integrity of the rabbit hutches you've built to house the fugitive rabbits is at risk because they can buckle when wet. Before the rabbits can be rescued from Professor Boolean's lab, you must compute how much standing water has accumulated on the rabbit hutches. 

Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top (and allowed to run off the sides). We'll assume all the hutches are square, have side length 1, and for the purposes of this problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] (the hutches are shown below):

...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123

When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:

...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123

The amount of water that has accumulated is the number of Os, which, in this instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as a list, computes the total area of standing water accumulated when water is poured from the top and allowed to run off the sides. 

The heights array will have at least 1 element and at most 9000 elements. Each element will have a value of at least 1, and at most 100000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) heights = [1, 4, 2, 5, 1, 2, 3]
Output:
    (int) 5

Inputs:
    (int list) heights = [1, 2, 3, 2, 1]
Output:
    (int) 0

"""

# first solution
def answer1(heights):

    # construct 2D array with placeholder 0
    array = [[ 0 for i in range(len(heights))] for j in range(max(heights))]

    # update array with 1 (representing X)
    for i in range(len(heights)):
        for j in range(-heights[i], 0):
            array[j][i] = 1

    # construct tracker: whenever sees 1, push the index to tracker
    tracker = [ [] for i in range(max(heights)) ]

    for i in range(len(array)):
        for j in range(len(heights)):
            if array[i][j] == 1:
                tracker[i].append(j)            

    # calculate number of 0s between two 1s
    counter = 0

    for i in range(len(tracker)):
        if len(tracker[i]) > 1:
            tracker[i].reverse()
            for j in range(len(tracker[i]) - 1):
                counter += (tracker[i][j] - tracker[i][j + 1] - 1)

    return counter


# second solution: to reduce memory used
def answer2(heights):

    # construct 2D array with placeholder 0
    array = [[0 for i in xrange(len(heights))] for j in xrange(max(heights))]

    # update array with 1 (representing X)
    for i in xrange(len(heights)):
        for j in xrange(-heights[i], 0):
            array[j][i] = 1

    # tracker is a re-usable list to remember 1's location on every list
    # counter is the number of 1s seen so far
    tracker = []
    counter = 0

    for i in xrange(len(array)):

        for j in xrange(len(heights)):
            if array[i][j] == 1:
                tracker.append(j)

        for y in xrange((len(tracker) - 1), 0, -1):
            counter += (tracker[y] - tracker[y - 1] - 1)

        tracker = []

    return counter


if __name__ == '__main__':
    print answer2([1, 4, 2, 5, 1, 2, 3])
    print answer2([1, 2, 3, 2, 1])
