"""
Solves a latin square.

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
import latinSquare


class Solver():

    def __init__(self):
        self.originalSq = latinSquare.LatinSquare()
        self.sovSq = None

    def __str__(self):
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
        self.originalSq.loadSquare(rawString)

    def randSquare(self, n, k, seed=None, randomise=True):
        self.originalSq.randSquare(n, k, seed, randomise)

    def solveSquare(self):
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
    print solv
    solv.solveSquare()
    print solv
