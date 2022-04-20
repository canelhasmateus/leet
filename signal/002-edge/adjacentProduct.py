import math


def solution( array ):
	prev = 1
	maxProd = -math.inf
	for current in array:
		prod = current * prev
		maxProd = prod if prod > maxProd else maxProd
		prev = current
	return maxProd


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( [ 3, 6, -2, -5, 7, 3 ] ) == 21

		def test2( self ):
			assert solution( [ -23, 4, -3, 8, -12 ] ) == -12

		def test3( self ):
			assert solution( [ 1, 0 , 1 , 0 , 1000 ] ) == 0


	unittest.main()
