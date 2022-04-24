def solution( param1, param2 ):
	...


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [0,4,3,1,2]), [0,1,1,1,2] )


	unittest.main()
