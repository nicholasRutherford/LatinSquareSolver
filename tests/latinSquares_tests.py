
from latinSquares import latinSquare


def test_hole():
    h = latinSquare.Hole(5)
    assert(len(h.options) == 5)


def test_isSolved():
    sq = latinSquare.LatinSquare(5, 1)
    assert(sq.isSolved())
    sq.grid[0][0] = 0
    assert(not sq.isSolved())

    # Hole with correct value is correct
    sq = latinSquare.LatinSquare(5, 1)
    h = latinSquare.Hole(5)
    h.value = 4
    sq.grid[0][0] = h
    assert(sq.isSolved())

    # Hole with wrong value is not correct
    sq = latinSquare.LatinSquare(5, 1)
    h = latinSquare.Hole(5)
    h.value = 0
    sq.grid[0][0] = h
    assert(not sq.isSolved())


def test_randomise():
    sq = latinSquare.LatinSquare(5, 1)
    sq.randomise()
    assert(sq.isSolved())


def test_checkHoleOptions():
    sq = latinSquare.LatinSquare(5, 1)
    h = sq.holes[0]
    h.x = 0
    h.y = 0
    sq.grid[0][0] = h
    sq.checkHoleOptions()
    assert(len(h.options) == 1)
    assert(h.options[0] == 4)

    sq = latinSquare.LatinSquare(5, 2, randomise=False)
    h1 = sq.holes[0]
    h1.x = 0
    h1.y = 0
    sq.grid[0][0] = h1

    h2 = sq.holes[1]
    h2.x = 1
    h2.y = 0
    sq.grid[1][0] = h2

    sq.checkHoleOptions()
    assert(len(h1.options) == 1)
    assert(h1.options[0] == 0)
    assert(len(h2.options) == 1)
    assert(h2.options[0] == 1)


def test_valid():
    sq = latinSquare.LatinSquare(5, 2, randomise=False)
    h1 = sq.holes[0]
    h1.x = 0
    h1.y = 0
    h1.valueSet = True
    h1.value = 1
    sq.grid[0][0] = h1

    h2 = sq.holes[1]
    h2.x = 1
    h2.y = 0
    sq.grid[1][0] = h2

    assert(not sq.isValid())
    h1.value = 0
    assert(sq.isValid())


def test_updateHoleOptions():
    sq = latinSquare.LatinSquare(5, 4, randomise=False)

    h1 = sq.holes[0]
    h1.x = 0
    h1.y = 0
    sq.grid[0][0] = h1

    h2 = sq.holes[1]
    h2.x = 3
    h2.y = 0
    sq.grid[3][0] = h2

    h3 = sq.holes[2]
    h3.x = 0
    h3.y = 3
    sq.grid[0][3] = h3

    h4 = sq.holes[3]
    h4.x = 3
    h4.y = 3
    sq.grid[3][3] = h4

    sq.checkHoleOptions()

    assert(len(h1.options) == 2)
    assert(h1.options[0] == 0)
    assert(h1.options[1] == 3)

    h1.value = 0
    h1.setValue = True
    sq.updateHoleOptions(h1)

    assert(len(h2.options) == 1)
    assert(h2.options[0] == 3)
