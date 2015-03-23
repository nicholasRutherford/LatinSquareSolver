
from timeit import timeit
HEADER = "n,k,"
FILENAME = "data.csv"

T = 10
for t in xrange(T):
    HEADER += "t" + str(t) + ","
HEADER = HEADER[:-1]

ofile = open(FILENAME, "w+")
ofile.write(HEADER + "\n")
for n in xrange(2,10):
    print n
    for k in xrange(1,n**2 -1):
        print "\t" + str(k)
        line = "{0},{1}".format(n,k)
        for t in xrange(T):
            st = """
            import latinSquare
            from solver import solve
            square = latinSquare.LatinSquare({0},{1}, seed = None)
            square.addHoles()
            solve(square)
            """.format(n,k)
            line += "," + str(timeit(st, number=1))
        ofile.write(line + "\n")
ofile.close()
