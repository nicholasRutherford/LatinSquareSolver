"""
Generates timing data for the solver.

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
from timeit import timeit

HEADER = "n,k,"
FILENAME = "15data.csv"

N_TO_TEST = [10]

# Set up header
TRIALS = 50
for t in xrange(TRIALS):
    HEADER += "t" + str(t) + ","
HEADER = HEADER[:-1]

ofile = open(FILENAME, "w+")
ofile.write(HEADER + "\n")
for n in N_TO_TEST:
    print n

    for k in range(1, n**2-1):
        print "\t" + str(k)
        line = "{0},{1}".format(n, k)

        for t in xrange(TRIALS):
            st = """
            import latinSquare
            from solver import solve
            square = latinSquare.LatinSquare({0},{1}, seed = None)
            square.addHoles()
            solve(square)
            """.format(n, k)
            line += "," + str(timeit(st, number=1))

        print "\t\t" + line[:20]
        ofile.write(line + "\n")
ofile.close()
