.. LatinSquareSolver documentation master file, created by
   sphinx-quickstart on Sat Apr 18 16:06:06 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to LatinSquareSolver's documentation!
=============================================
Looking to get started right away? Check out the :ref:`instillation-label`
and :ref:`quickstart-label` pages.

Latin Squares Explained
-----------------------

A Latin Square is a \\(N\\times N\\) matrix where each row, and each column
contains the numbers \\(\\left\\{ 1,2,\\dots,n\\right\\}\\). We then add in
\\(K\\) holes to the square that must be filled in so that each row and
column contain the numbers
\\(\\left\\{ 1,2,\\dots,n\\right\\}\\). An example Latin Square with
\\(N=5,\\text{ and }K=16\\) is:

$$\\begin{array}{ccccc}
\\square & 2 & \\square & \\square & 4\\\\
3 & \\square & 1 & \\square & \\square\\\\
\\square & 4 & \\square & \\square & 1\\\\
2 & \\square & \\square & \\square & 3\\\\
\\square & \\square & 2 & 1 & \\square
\\end{array}$$


And the solution would be:

$$\\begin{array}{ccccc}
1 & 2 & 5 & 3 & 4\\\\
3 & 5 & 1 & 4 & 2\\\\
5 & 4 & 3 & 2 & 1\\\\
2 & 1 & 4 & 5 & 3\\\\
4 & 3 & 2 & 1 & 5
\\end{array}$$

How The Solver Works
--------------------
The initial solution to this problem would be to use depth first search to
iterate through all the possible values for each hole. Unfortunately the
complexity of this problem will cause depth first search to take an infeasible
amount of time for even small problems like the one shown above. Since brute
force depth first search is out of the question we need to come up with clever
methods to help it out and this is done with two main methods, forward
checking, and arc consistency. When we are filling in values to the
Latin Square we have to make two decisions per branch, which hole to fill,
and what value to put into the hole. We use forward checking to make sure
that we select the hole, and value for that hole that has the highest
probability of being correct. Arc Consistency is used to keep track of
what the valid values would be for each hole, and to update this list of
values as we fill in the square.

License:
--------
.. image:: ./images/gplv3.png
This software is licensed under GPLv3. For the full license
see: :ref:`license-label`

Contents:
---------

.. toctree::
   :maxdepth: 2

   instillation
   quickstart
   latinSquares
   extraInfo
   license
