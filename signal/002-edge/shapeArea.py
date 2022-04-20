import math


def solution( param1 ):
	return math.floor( math.sqrt( 2 ) * param1 * param1 )


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( 2 ) == 5


	unittest.main()
