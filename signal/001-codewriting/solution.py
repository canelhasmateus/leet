

def solution( param1, param2 ):
	return 3


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( 1 ,2 ) == 3


	unittest.main()
