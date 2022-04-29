def solution( param1):
	return False


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( 248622), True )


	unittest.main()
