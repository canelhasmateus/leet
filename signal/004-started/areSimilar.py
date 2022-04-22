def solution( param1, param2 ):
	return False


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 1 , 2 , 3 ] , [ 1, 2 , 3]), True )


	unittest.main()
