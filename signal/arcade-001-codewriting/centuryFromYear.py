import math


def solution( year ):
	return math.ceil( year / 100 )


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( 1905 ) == 20
		def test2( self ):
			assert solution( 1700 ) == 17


	unittest.main()
