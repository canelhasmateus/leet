def solution( array ):
	prev = 1
	maxProd = 0
	for current in array:
		prod = current * prev
		if (prod > maxProd) :
			maxProd = prod
		prev = current
	return maxProd


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( [ 3 , 6 , -2 , -5 , 7 , 3 ] == 21 )


	unittest.main()
