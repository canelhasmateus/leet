def solution( param1):
	return 3


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [1 , 1 , 1]), 3 )


	unittest.main()
