from nose.tools import raises

from LatinSquareSolver import latinSquare
import random


def test_hole():
    """Hole"""
    h = latinSquare.Hole(5)
    assert(len(h.options) == 5)


def test_isSolved():
    """isSolved()"""
    sq = latinSquare.LatinSquare()
    sq.randSquare(5, 1, randomise=False, seed=1337)
    assert(not sq.isSolved())
    sq.holes[0].value = 3
    sq.holes[0].valueSet = True
    assert(sq.isSolved())

    # Hole with correct value is correct
    sq = latinSquare.LatinSquare()
    n = 5
    sq.n = n
    sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]
    h = latinSquare.Hole(n)
    h.value = 0
    sq.grid[0][0] = h
    assert(sq.isSolved())

    # Hole with wrong value is not correct
    sq = latinSquare.LatinSquare()
    n = 5
    sq.n = n
    sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]
    h = latinSquare.Hole(n)
    h.value = 4
    sq.grid[0][0] = h
    assert(not sq.isSolved())


def test_randomise():
    """randomise()"""
    sq = latinSquare.LatinSquare()
    sq.randSquare(5, 1, randomise=False, seed=1337)
    sq.randomise()
    assert(sq.isValid())


def test_checkHoleOptions():
    """chechHoleOptions)"""
    sq = latinSquare.LatinSquare()
    n = 5
    sq.n = n
    sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]

    h = latinSquare.Hole(n)
    sq.holes.append(h)
    h.x = 0
    h.y = 0
    sq.grid[0][0] = h
    sq.checkHoleOptions()
    assert(len(h.options) == 1)
    assert(h.options[0] == 0)

    sq = latinSquare.LatinSquare()
    n = 5
    sq.n = n
    sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]

    h1 = latinSquare.Hole(n)
    sq.holes.append(h1)
    h1.x = 0
    h1.y = 0
    sq.grid[0][0] = h1

    h2 = latinSquare.Hole(n)
    sq.holes.append(h2)
    h2.x = 1
    h2.y = 0
    sq.grid[1][0] = h2

    sq.checkHoleOptions()
    assert(len(h1.options) == 1)
    assert(h1.options[0] == 0)
    assert(len(h2.options) == 1)
    assert(h2.options[0] == 1)


def test_isValid():
    """isValid()"""
    sq = latinSquare.LatinSquare()
    n = 5
    sq.n = n
    sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]

    h1 = latinSquare.Hole(n)
    sq.holes.append(h1)
    h1.x = 0
    h1.y = 0
    h1.valueSet = True
    h1.value = 1
    sq.grid[0][0] = h1

    h2 = latinSquare.Hole(n)
    sq.holes.append(h2)
    h2.x = 1
    h2.y = 0
    sq.grid[1][0] = h2

    assert(not sq.isValid())
    h1.value = 0
    assert(sq.isValid())


def test_updateHoleOptions():
    """updateHoleOptions()"""
    sq = latinSquare.LatinSquare()
    n = 5
    sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]

    h1 = latinSquare.Hole(n)
    sq.holes.append(h1)
    h1.x = 0
    h1.y = 0
    sq.grid[0][0] = h1

    h2 = latinSquare.Hole(n)
    sq.holes.append(h2)
    h2.x = 3
    h2.y = 0
    sq.grid[3][0] = h2

    h3 = latinSquare.Hole(n)
    sq.holes.append(h3)
    h3.x = 0
    h3.y = 3
    sq.grid[0][3] = h3

    h4 = latinSquare.Hole(n)
    sq.holes.append(h4)
    h4.x = 3
    h4.y = 3
    sq.grid[3][3] = h4

    sq.checkHoleOptions()

    print len(h1.options)
    print h1.options
    assert(len(h1.options) == 2)
    assert(h1.options[0] == 0)
    assert(h1.options[1] == 3)

    h1.value = 0
    h1.setValue = True
    sq.updateHoleOptions(h1)

    assert(len(h2.options) == 1)
    assert(h2.options[0] == 3)


def test_addHoles():
    """addHoles()"""
    for i in xrange(1, 5**2):
        random.seed(i)
        sq = latinSquare.LatinSquare()
        n = 5
        k = i
        sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]
        sq.n = n
        sq.k = k
        sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]
        sq.holes = [latinSquare.Hole(n) for x in range(k)]
        sq.addHoles()
        assert(len(sq.holes) == i)


def test_randSquare():
    """randSquare()"""
    n = 5
    k = 7
    sq = latinSquare.LatinSquare()
    sq.randSquare(n, k, seed=1337, randomise=False)

    assert(sq.isValid())
    assert(len(sq.holes) == k)
    assert(sq.n == n)
    good = range(n)
    for i, x in enumerate(sq.grid[0]):
        if not isinstance(x, latinSquare.Hole):
            assert(x == good[i])

    sq = latinSquare.LatinSquare()
    sq.randSquare(n, k, seed=1337)

    assert(sq.isValid())
    assert(len(sq.holes) == k)
    assert(sq.n == n)
    good = range(n)
    allMatch = True
    for i, x in enumerate(sq.grid[0]):
        if x != good[i]:
            allMatch = False
    assert(not allMatch)


def test_strHoles():
    """strHoles()"""
    good = ("4 * * 3 *\n"
            "1 * * 0 2\n"
            "2 0 4 * *\n"
            "0 3 2 * 1\n"
            "3 1 * * 4")
    sq = latinSquare.LatinSquare()
    sq.randSquare(5, 10, seed=1337)
    assert (good == sq.strHoles())


def test_validHoles():
    """validHoles()"""
    sq = latinSquare.LatinSquare()
    n = 5
    sq.n = n
    sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]

    h1 = latinSquare.Hole(n)
    sq.holes.append(h1)
    h1.x = 0
    h1.y = 0
    h1.value = 1
    h1.valueSet = True
    sq.grid[0][0] = h1

    h2 = latinSquare.Hole(n)
    sq.holes.append(h2)
    h2.x = 0
    h2.y = 1
    sq.grid[0][1] = h2

    sq.checkHoleOptions()
    sq.updateHoleOptions(h1)
    assert(len(sq.holes[1].options) == 0)
    assert(not sq.validHoles())

    h1.value = 0
    h2.options = range(n)
    sq.checkHoleOptions()
    sq.updateHoleOptions(h1)
    assert(len(sq.holes[1].options) == 1)
    assert(sq.validHoles())


def test_validRows():
    """validRows()"""
    sq = latinSquare.LatinSquare()
    n = 5
    sq.n = n
    sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]

    h1 = latinSquare.Hole(n)
    sq.holes.append(h1)
    h1.x = 0
    h1.y = 0
    h1.value = 3
    h1.valueSet = True
    sq.grid[0][0] = h1

    h2 = latinSquare.Hole(n)
    sq.holes.append(h2)
    h2.x = 0
    h2.y = 1
    sq.grid[0][1] = h2

    sq.checkHoleOptions()
    sq.updateHoleOptions(h1)
    assert(not sq.validRows())
    h1.value = 0
    assert(sq.validRows())
    h1.value = 1
    assert(sq.validRows())


def test_validCols():
    """validCols()"""
    sq = latinSquare.LatinSquare()
    n = 5
    sq.n = n
    sq.grid = [[(x+y) % n for x in range(n)] for y in range(n)]

    h1 = latinSquare.Hole(n)
    sq.holes.append(h1)
    h1.x = 0
    h1.y = 0
    h1.value = 3
    h1.valueSet = True
    sq.grid[0][0] = h1

    h2 = latinSquare.Hole(n)
    sq.holes.append(h2)
    h2.x = 1
    h2.y = 0
    sq.grid[1][0] = h2

    sq.checkHoleOptions()
    sq.updateHoleOptions(h1)
    assert(not sq.validCols())
    h1.value = 0
    assert(sq.validCols())
    h1.value = 1
    assert(sq.validCols())


def test_nextStates():
    """nextStates()"""
    sq = latinSquare.LatinSquare()
    sq.randSquare(5, 10, seed=1337)
    newSqList = []
    for x in sq.nextStates():
        newSqList.append(x)
    assert(len(newSqList) == 1)

    newSq = newSqList[0]
    count = 0
    for h in newSq.holes:
        if h.valueSet is False:
            count += 1
    assert(count == 9)

    count = 0
    for h in sq.holes:
        if h.valueSet is False:
            count += 1
    assert(count == 10)


def test_loadSqaure():
    """loadSquare()"""
    square = ("0 1 2 3 4\n"
              "1 2 3 4 _\n"
              "* 3 4 0 1\n"
              "3 4 0 1 2\n"
              "4 0 % 2 3")

    goodStr = ("0 1 2 3 4\n"
               "1 2 3 4 *\n"
               "* 3 4 0 1\n"
               "3 4 0 1 2\n"
               "4 0 * 2 3")

    sq = latinSquare.LatinSquare()
    sq.loadSquare(square)
    assert(sq.strHoles() == goodStr)


@raises(RuntimeError)
def test_failLoadSquareUnevenRows():
    """loadSquare() - fail1"""
    square = ("0 1 2 3 4\n"
              "1 2 3 4 _\n"
              "* 3 4 0 1\n"
              "3 4 0 1\n"
              "4 0 % 2 3")

    sq = latinSquare.LatinSquare()
    sq.loadSquare(square)


@raises(RuntimeError)
def test_failLoadSquareInvalidSquare():
    """loadSquare() - fail2"""
    square = ("1 1 2 3 4\n"
              "1 2 3 4 _\n"
              "* 3 4 0 1\n"
              "3 4 0 1 2\n"
              "4 0 % 2 3")

    sq = latinSquare.LatinSquare()
    sq.loadSquare(square)
