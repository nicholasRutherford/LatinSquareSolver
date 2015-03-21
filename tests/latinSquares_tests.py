from nose.tools import raises, timed
import latinSquares

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

@timed(2)
def test_basic():
    assert(True)

@raises (ValueError)
def test_exception():
    raise ValueError("eek")