def solution( param1 ):
	return 2 * param1 * (param1 - 1) + 1


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test0( self ):
			self.assertEqual( solution( 1 ), 1 )

		def test1( self ):
			self.assertEqual( solution( 2 ), 5 )

		def test2( self ):
			self.assertEqual( solution( 3 ), 13 )


	unittest.main()
