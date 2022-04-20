

def solution( param1, param2 ):
	x = 3
	return x


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( 1 ,2 ) == 3


	unittest.main()
