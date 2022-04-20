def solution( year):
	return year



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			assert solution( 1905 ) == 20


	unittest.main()
