

def solution( param1, param2 ):
	return param1 + param2


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( 1 ,2 ) == 3

		def test2( self ):
			assert solution( 2 , 3 ) == 4


	unittest.main()
