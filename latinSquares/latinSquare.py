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
from collections import Counter

class Hole:

    def __init__(self, n):
        self.value = 0
        self.valueSet = False
        self.options = range(n)
        self.x = 0
        self.y = 0

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
            self.holes[i].x = x
            self.holes[i].y = y
            self.grid[x][y] = self.holes[i]
        self.checkHoleOptions()

    def __init__(self, n, k, seed=1337, randomise=True):
        random.seed(seed)
        self.n = n
        self.k = k
        self.grid = [[(x+y)% n for x in range(n)] for y in range(n)]
        if randomise:
            self.randomise()
        self.holes = [Hole(n) for x in range(k)]

    def __str__(self):
        output = ""
        spacing = int(math.ceil(math.log10(self.n)))
        for row in self.grid:
            for ele in row:
                if isinstance(ele, Hole):
                    output += ("{:>" +str(spacing) + "}").format(ele) + "'"
                else:
                    output += ("{:>" +str(spacing) + "}").format(ele) + " "
            output += "\n"
        return output[:-1] #Ignore last newline

    def strHoles(self):
        output = ""
        spacing = int(math.ceil(math.log10(self.n)))
        for row in self.grid:
            for ele in row:
                if isinstance(ele, Hole):
                    output +=  ("{:>" +str(spacing) + "}").format("*") + " "
                else:
                    output +=  ("{:>" +str(spacing) + "}").format(ele) + " "
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

    def isValid(self):
        # Check Holes
        for hole in self.holes:
            if not hole.valueSet and len(hole.options) == 0:
                return False

        # Verify rows
        for row in self.grid:
            rowEle = []
            for ele in row:
                if not isinstance(ele, Hole):
                    rowEle.append(ele)
                elif ele.valueSet:
                    rowEle.append(ele.value)
            if any([x[1]>1 for x in Counter(rowEle).items()]):
                return False

        # Verify col
        for i in range(self.n):
            colEle = []
            col = [x[i] for x in self.grid]
            for ele in col:
                if not isinstance(ele, Hole):
                    colEle.append(ele)
                elif ele.valueSet:
                    colEle.append(ele.value)
            if any([x[1]>1 for x in Counter(colEle).items()]):
                return False
        return True


    def nextStates(self):

        # Sort holes so that the hole with the least number of
        # options is looked at first
        self.holes.sort(key = lambda x : len(x.options))

        for i, hole in enumerate(self.holes):
            if hole.valueSet:
                continue
            for opt in hole.options:
                newState = deepcopy(self)
                newState.holes[i].value = opt
                newState.holes[i].valueSet = True
                newState.updateHoleOptions(newState.holes[i])
                yield newState
            break

    def checkHoleOptions(self):
        for hole in self.holes:
            invalid = []
            for ele in self.grid[hole.x]:
                if not isinstance(ele, Hole):
                    invalid.append(ele)

            for row in self.grid:
                ele  = row[hole.y]
                if not isinstance(ele, Hole):
                    invalid.append(ele)

            good = []
            for ele in hole.options:
                if ele not in invalid:
                    good.append(ele)
            hole.options = good


    def updateHoleOptions(self, h):
        for hole in self.holes:
            if hole.valueSet:
                continue
            if not( hole.x == h.x or hole.y == h.y):
                continue
            if (hole.x ==h.x and hole.y==h.y):
                continue
            while hole.options.count(h.value) > 0:
                hole.options.remove(h.value)



if __name__ == "__main__":
    sq = LatinSquare(5, 1, seed=1337)
    sq.addHoles()
    print "Initial square"
    print sq
    print "\nPossilbe squares:"
    for st in sq.nextStates():
        print st
        print ""
