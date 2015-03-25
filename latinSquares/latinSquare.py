"""
Represents a Latin Square and includes methods needed to search for a solution

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
    """Represent a square in a latin square that needs to be filled in,
        aka a hole in the square.

        Keeps track of the location of the hole, the possible
        values that the hole can take, and whether the value has been set.
    """

    def __init__(self, n):
        """ Inititialize a hole in a Latin Square

        Args:
            n (int) - The size of the latin square
        """
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
        """Takes a correct latin square and randomises the entries.

        The randomization is done by performing an in place randomization
        of the rows, and then of the columns. As long as the latin square
        was valid before, it will be valid afterwards.
        """
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
        """Randomly initializes the holes in the grid.

        This randomly adds K holes to the graph. The result will be a
        solveable latin square, but there may be more then one solution
        to it.
        """
        possibleOptions = range(self.n ** 2)  # There are n^2 grid locations
        selections = random.sample(possibleOptions, self.k)

        for i, opt in enumerate(selections):
            x = opt / self.n
            y = opt % self.n
            self.holes[i].x = x
            self.holes[i].y = y
            self.grid[x][y] = self.holes[i]
        self.checkHoleOptions()

    def __init__(self, n, k, seed=1337, randomise=True):
        """Initialize a latin square.

        Args:
            n (int) - The side length of the square
            k (int) - The number of holes in the grid
            seed - The seed for the random number generator
            randomise (bool) - Whether to randomise the grid, or leave with
                                the basic grid layout

        If randomise is not selected the square will remain in the basic
        state where each row is one offset from the previous. Ie for N = 5:
        0 1 2 3 4
        1 2 3 4 0
        2 3 4 0 1
        3 4 0 1 2
        4 0 1 2 3
        """
        random.seed(seed)
        self.n = n
        self.k = k
        self.grid = [[(x+y) % n for x in range(n)] for y in range(n)]
        if randomise:
            self.randomise()
        self.holes = [Hole(n) for x in range(k)]

    def __str__(self):
        """Pretty output. Hole values are postfixed with '."""
        output = ""
        spacing = int(math.ceil(math.log10(self.n)))
        for row in self.grid:
            for ele in row:
                if isinstance(ele, Hole):
                    output += ("{:>" + str(spacing) + "}").format(ele) + "'"
                else:
                    output += ("{:>" + str(spacing) + "}").format(ele) + " "
            output += "\n"
        return output[:-1]  # Ignore last newline

    def strHoles(self):
        """Pretty output. Holes are marked with an *."""
        output = ""
        spacing = int(math.ceil(math.log10(self.n)))
        for row in self.grid:
            for ele in row:
                if isinstance(ele, Hole):
                    output += ("{:>" + str(spacing) + "}").format("*") + " "
                else:
                    output += ("{:>" + str(spacing) + "}").format(ele) + " "
            output += "\n"
        return output[:-1]  # Ignore last newline

    def isSolved(self):
        """Determine is the current square is correctly solved

        Returns:
            bool. True if it is correctly solved, False otherwise.

        Determines if the square is correct by making sure that each
        row and column contains all of the elements from 0 to n.
        This method will fail quicker than counting the values for
        each row and column and making sure there are no duplicates.
        """
        good = range(self.n)

        # Check rows
        for row in self.grid:
            for ele in good:
                if ele not in row:
                    return False

        # Check col
        for i in range(self.n):
            col = [x[i] for x in self.grid]
            for ele in good:
                if ele not in col:
                    return False
        return True

    def validHoles(self):
        """Determine if the values for the holes is valid.

        Returns:
            bool. If the holes have valid values will return True,
                    False otherwise.

        Determines validatiy by checking that each non-set hole
        has at least one option for it's value.
        """
        for hole in self.holes:
            if not hole.valueSet and len(hole.options) == 0:
                return False
        return True

    def validRows(self):
        """ Determines whether the rows are valid.

        Returns:
            bool. True if the rows are valid, False otherwise.

        Determines validitity by making sure no value is repeated twice in
        each row. This is more expensive than the method used in isSolved, but
        nessesary since there could be holes in the grid.
        """
        for row in self.grid:
            rowEle = []
            for ele in row:
                if not isinstance(ele, Hole):
                    rowEle.append(ele)
                elif ele.valueSet:
                    rowEle.append(ele.value)
            if any([x[1] > 1 for x in Counter(rowEle).items()]):
                return False
        return True

    def validCols(self):
        """ Determines whether the columns are valid.

        Returns:
            bool. True if the columns are valid, False otherwise.

        Determines validitity by making sure no value is repeated twice in
        each column. This is more expensive than the method used
        in isSolved, but nessesary since there could be holes in the grid.
        """
        for i in range(self.n):
            colEle = []
            col = [x[i] for x in self.grid]
            for ele in col:
                if not isinstance(ele, Hole):
                    colEle.append(ele)
                elif ele.valueSet:
                    colEle.append(ele.value)
            if any([x[1] > 1 for x in Counter(colEle).items()]):
                return False
        return True

    def isValid(self):
        """Whether a partially filled in latin square has valid hole values

        Returns:
            bool. True if everything is valid so far, False otherwise
        """

        if not self.validHoles():
            return False
        elif not self.validRows():
            return False
        elif not self.validCols():
            return False
        return True

    def nextStates(self):
        """Generate all the squares corresponding to the options of the
            hole with the least number of options.

        Returns:
            [latinSquare]. List of squares corresponding to selecting
                            one of the possible values of the hole h,
                            where h has the smallest number of possible
                            values out of all the holes.

        The list of squares is calculated lazily, where the value is not
        calculated until it is actually used. This cuts down on the
        number of expensive deepcopy calls needed.
        """

        # Sort holes so that the hole with the least number of
        # options is looked at first
        self.holes.sort(key=lambda x: len(x.options))

        # Find the hole with the least number of options
        # that hasn't had it's value set
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
        """Removes possible options from each hole based on the non-hole
            values.
        """
        for hole in self.holes:
            invalid = []
            for ele in self.grid[hole.x]:
                if not isinstance(ele, Hole):
                    invalid.append(ele)

            for row in self.grid:
                ele = row[hole.y]
                if not isinstance(ele, Hole):
                    invalid.append(ele)

            good = []
            for ele in hole.options:
                if ele not in invalid:
                    good.append(ele)
            hole.options = good

    def updateHoleOptions(self, h):
        """Removes possible options from each hole based on the values of
        the holes with their value set.
        """
        for hole in self.holes:
            if hole.valueSet:
                continue
            if not(hole.x == h.x or hole.y == h.y):
                continue
            if (hole.x == h.x and hole.y == h.y):
                continue
            while hole.options.count(h.value) > 0:
                hole.options.remove(h.value)
