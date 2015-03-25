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


def solve(sq):
    if sq.isSolved():
        return sq
    else:
        for state in sq.nextStates():
            # Check if the state is valid
            if not state.isValid():
                continue

            sol = solve(state)
            if sol is None:
                continue
            else:
                return sol
        # If there are no nextStates
        return None

if __name__ == "__main__":
    square = latinSquare.LatinSquare(25, 50, seed=1337)

    print "Initial Square:"
    print square

    square.addHoles()
    print "\nPuzzel to Solve: "
    print square.strHoles()

    print "\nSolution Found: "
    print solve(square)
