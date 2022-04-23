def solution( param1 ):
	return 0

if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution([5,3,6,7,9]), 4 )


	unittest.main()
