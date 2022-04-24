def solution( message ):

	return message


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "codesignal") , "cadosegnil")


	unittest.main()
