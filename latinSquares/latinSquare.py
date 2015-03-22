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

class Hole:

    def __init__(self):
        self.verified = False
        self.options = []
        self.value = -1

    def __str__(self):
        if self.value == -1:
            return " "
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

        for opt in selections:
            print opt
            x = opt / self.n
            y = opt % self.n
            self.grid[x][y] = Hole()


    def __init__(self, n, k, seed=1337):
        random.seed(seed)
        self.n = n
        self.grid = [[(x+y)% n for x in range(n)] for y in range(n)]
        self.randomise()
        self.addHoles(k)

    def __str__(self):
        output = ""
        for row in self.grid:
            for ele in row:
                output += " " + str(ele)
            output += "\n"
        return output[:-1] #Ignore last newline

if __name__ == "__main__":
    sq = LatinSquare(5, 5, seed=1337)
    print sq
