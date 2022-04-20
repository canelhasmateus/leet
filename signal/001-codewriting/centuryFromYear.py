import math


def solution( year ):
	return 1 + math.floor( year / 100 )


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( 1905 ) == 20


	unittest.main()
