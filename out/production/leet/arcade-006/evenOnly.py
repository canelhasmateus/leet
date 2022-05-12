def solution( number ):
	for character in str( number ):
		if (int( character) % 2 != 0):
			return False
	return True


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( 248622), True )


	unittest.main()
