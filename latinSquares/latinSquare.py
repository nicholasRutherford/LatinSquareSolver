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

class Hole:

    def __init__(self):
        self.verified = False
        self.options = []
        self.value = None

    def __str__(self):
        if self.value is None:
            return "*"
        else:
            return str(self.value)


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

    def addHoles(self, k):
        possibleOptions = range(self.n ** 2)
        selections = random.sample(possibleOptions, k)

        for i, opt in enumerate(selections):
            x = opt / self.n
            y = opt % self.n
            self.grid[x][y] = self.holes[i]

    def __init__(self, n, k, seed=1337):
        random.seed(seed)
        self.n = n
        self.grid = [[(x+y)% n for x in range(n)] for y in range(n)]
        self.randomise()
        self.holes = [Hole() for x in range(k)]
        self.addHoles(k)

    def __str__(self):
        output = ""
        spacing = int(math.ceil(math.log10(self.n)))
        for row in self.grid:
            for ele in row:
                output += " " + ("{:>" +str(spacing) + "}").format(ele)
            output += "\n"
        return output[:-1] #Ignore last newline

    def isEndState(self):
        for hole in self.holes:
            if hole.value is None:
                return False
        return True

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

if __name__ == "__main__":
    sq = LatinSquare(11, 5, seed=1337)
    print sq
