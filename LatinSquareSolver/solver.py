"""
Solves a latin square.
"""
# Copyright (C) 2015  Nicholas Rutherford
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import latinSquare


class Solver():

    def __init__(self):
        """Initialize a solver in order to solve a latin square."""

        self.originalSq = latinSquare.LatinSquare()
        self.sovSq = None

    def __str__(self):
        """Pretty output"""
        if not self.originalSq.loaded:
            print "No square loaded. Run 'loadSquare' or 'randSquare' first"
            return ""

        toOut = "Original Square:\n"
        toOut += self.originalSq.strHoles() + "\n"

        if self.sovSq is None:
            return toOut
        else:
            toOut += "\nSolved Square:\n"
            toOut += str(self.sovSq)
            return toOut

    def loadSquare(self, rawString):
        """Load a latin square from a string

        Args:
            rawStr (str): The latin square as string

        Notes:
            The elements must be intgers seperated by spaces. The holes
            are denoted as non-integer, non-space elements, such as '*', or
            '_'. For example::

                0 1 2 3 4
                1 2 3 4 _
                2 3 4 0 1
                3 4 0 1 2
                4 0 1 2 3
        """
        self.originalSq.loadSquare(rawString)

    def randSquare(self, n, k, seed=None, randomise=True):
        """Initialize a random latin square.

        Args:
            n (int): The side length of the square
            k (int): The number of holes in the grid
            seed (int): The seed for the random number generator
            randomize (bool): Whether to randomize the grid, or leave with
                                the basic grid layout

        Notes:
            The Latin Square generated will be solveable, though the
            solution is not guarteed to be unique.
            If randomize is not selected the square will remain in the basic
            state where each row is one offset from the previous.
            Ie for N = 5::

                0 1 2 3 4
                1 2 3 4 0
                2 3 4 0 1
                3 4 0 1 2
                4 0 1 2 3
        """
        self.originalSq.randSquare(n, k, seed, randomise)

    def solveSquare(self):
        """Solve the loaded latin square."""

        if not self.originalSq.loaded:
            print "Error: No square loaded."
        else:
            self.sovSq = self._solve(self.originalSq)

    def _solve(self, sq):
        """Solve a Latin square.

        Args:
            sq (latinSquare): The square to solve.

        Returns:
            latinSquare: The solution to the initial square
        """
        if sq.isSolved():
            return sq
        else:
            for state in sq.nextStates():
                # Check if the state is valid
                if not state.isValid():
                    continue

                sol = self._solve(state)
                if sol is None:
                    continue
                else:
                    return sol
            # If there are no nextStates
            return None

if __name__ == "__main__":

    square = ("0 1 2 3 4\n"
              "1 2 3 4 _\n"
              "2 3 4 0 1\n"
              "3 4 0 1 2\n"
              "4 0 1 2 3")

    solv = Solver()
    # solv.randSquare(10, 25)
    solv.loadSquare(square)
    solv.solveSquare()
    print solv
