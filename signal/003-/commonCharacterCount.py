def solution( param1, param2 ):
	return 0


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "aabcc" , "adcaa"), 3 )


	unittest.main()
