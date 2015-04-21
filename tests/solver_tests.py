# from latinSquares import latinSquare
from LatinSquareSolver import solver


def test_solveSquare():
    """solveSquare()"""
    square = ("0 1 2 3 4\n"
              "1 2 3 4 _\n"
              "2 3 4 0 1\n"
              "3 4 0 1 2\n"
              "4 0 1 2 3")
    goodStr = ("0 1 2 3 4 \n"
               "1 2 3 4 0'\n"
               "2 3 4 0 1 \n"
               "3 4 0 1 2 \n"
               "4 0 1 2 3 ")

    solv = solver.Solver()
    solv.loadSquare(square)
    solv.solveSquare()
    assert(str(solv.sovSq) == goodStr)

    goodStr = ("4 2'1'3 0'\n"
               "1 4'3'0 2 \n"
               "2 0 4 1'3'\n"
               "0 3 2 4'1 \n"
               "3 1 0'2'4 ")

    solv = solver.Solver()
    solv.randSquare(5, 10, seed=1337)
    solv.solveSquare()
    assert(str(solv.sovSq) == goodStr)
