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
import latinSquare

def solve(sq):
    if sq.isCorrect():
        print "found correct"
        return sq
    else:
        for state in sq.nextStates():
            sol = solve(state)
            if sol is None:
                continue
            else:
                return sol

if __name__ == "__main__":
    square = latinSquare.LatinSquare(5,2)
    print "Initial Square:"
    print square
    square.addHoles()
    print "\nPuzzel: "
    print square.strHoles()
    print "\nSolution: "
    print solve(square)
