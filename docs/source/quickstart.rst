.. _quickstart-label:

Quickstart
===========

Example loading an already made square:
---------------------------------------
::

    square = ('0 1 2 3 4\\n'
              '1 2 3 4 _\\n'
              '2 3 4 0 1\\n'
              '3 4 0 1 2\\n'
              '4 0 1 2 3')

    solv = Solver()
    solv.loadSquare(square)
    solv.solveSquare()
    print solv

    >>>
    Original Square:
    0 1 2 3 4
    1 2 3 4 *
    2 3 4 0 1
    3 4 0 1 2
    4 0 1 2 3

    Solved Square:
    0 1 2 3 4
    1 2 3 4 0'
    2 3 4 0 1
    3 4 0 1 2
    4 0 1 2 3


Example with a randomly generated square:
-----------------------------------------
::

    solv = Solver()
    solv.randSquare(10, 25) # 10 x 10 square with 25 holes
    solv.solveSquare()
    print solv

    >>>
    Original Square:
    3 * * * 7 * * * * 2
    8 9 6 5 2 * 3 4 1 7
    6 * 4 3 0 8 1 * 9 5
    2 3 * 9 6 * * 8 * 1
    0 1 * 7 4 2 5 6 3 *
    4 5 2 1 * 6 9 0 7 3
    * 8 5 4 1 9 2 3 * 6
    1 2 * * 5 3 6 7 * 0
    9 0 7 6 3 1 4 * 2 8
    5 6 3 2 9 7 0 1 * *

    Solved Square:
    3 4'1'0'7 5'8'9'6'2
    8 9 6 5 2 0'3 4 1 7
    6 7'4 3 0 8 1 2'9 5
    2 3 0'9 6 4'7'8 5'1
    0 1 8'7 4 2 5 6 3 9'
    4 5 2 1 8'6 9 0 7 3
    7'8 5 4 1 9 2 3 0'6
    1 2 9'8'5 3 6 7 4'0
    9 0 7 6 3 1 4 5'2 8
    5 6 3 2 9 7 0 1 8'4'
