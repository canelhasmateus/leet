def solution( array ):
	return 0


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( [ 3 , 6 , -2 , -5 , 7 , 3 ] == 21 )


	unittest.main()
