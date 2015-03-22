"""
{one line to give the program's name and a brief idea of what it does.}
Copyright (C) 2015  Nicholas Rutherford

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import random
import math
from copy import deepcopy

class Hole:

    def __init__(self):
        self.verified = False
        self.options = []
        self.value = 0

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other



class LatinSquare:

    def randomise(self):
        # Randomise rows
        for x in range(self.n - 1):
            swapRow = random.randrange(x+1, self.n)
            for i in range(self.n):
                temp = self.grid[x][i]
                self.grid[x][i] = self.grid[swapRow][i]
                self.grid[swapRow][i] = temp

        # Randomise col
        for x in range(self.n - 1):
            swapCol = random.randrange(x+1, self.n)
            for i in range(self.n):
                temp = self.grid[i][x]
                self.grid[i][x] = self.grid[i][swapCol]
                self.grid[i][swapCol] = temp

    def addHoles(self):
        possibleOptions = range(self.n ** 2)
        selections = random.sample(possibleOptions, self.k)

        for i, opt in enumerate(selections):
            x = opt / self.n
            y = opt % self.n
            self.grid[x][y] = self.holes[i]

    def __init__(self, n, k, seed=1337):
        random.seed(seed)
        self.n = n
        self.k = k
        self.grid = [[(x+y)% n for x in range(n)] for y in range(n)]
        self.randomise()
        self.holes = [Hole() for x in range(k)]

    def __str__(self):
        output = ""
        spacing = int(math.ceil(math.log10(self.n)))
        holeBefore = False
        for row in self.grid:
            for ele in row:
                if holeBefore:
                    output += "'" + ("{:>" +str(spacing) + "}").format(ele)
                    holeBefore = False
                else:
                    output += " " + ("{:>" +str(spacing) + "}").format(ele)
                if isinstance(ele, Hole):
                    holeBefore = True
            output += "\n"
        return output[:-1] #Ignore last newline

    def strHoles(self):
        output = ""
        spacing = int(math.ceil(math.log10(self.n)))
        for row in self.grid:
            for ele in row:
                if isinstance(ele, Hole):
                    output += " *"
                else:
                    output += " " + ("{:>" +str(spacing) + "}").format(ele)
            output += "\n"
        return output[:-1] #Ignore last newline


    def isCorrect(self):
        # Verify rows
        good = range(self.n)
        for row in self.grid:
            for ele in good:
                if ele not in row:
                    return False

        # Verify col
        for i in range(self.n):
            col = [x[i] for x in self.grid]
            for ele in good:
                if ele not in col:
                    return False
        return True

    def nextStates(self):
        for i, hole in enumerate(self.holes):
            if hole.value != self.n -1:
                newState = deepcopy(self)
                newState.holes[i].value += 1
                yield newState


if __name__ == "__main__":
    sq = LatinSquare(5, 2, seed=1337)
    sq.addHoles()
    print "Initial square"
    print sq
    print "\nPossilbe squares:"
    for st in sq.nextStates():
        print st
        print ""
