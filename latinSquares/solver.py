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
        self.originalSq = None
        self.sovSq = None

    def __str__(self):
        pass

    def loadSquare(self, rawString):
        pass

    def solveSquare(self):
        pass

    def solve(self, sq):
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

                sol = self.solve(state)
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
    solv.loadSolver(square)
    solv.solve()
