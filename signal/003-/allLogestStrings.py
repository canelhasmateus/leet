def solution( strings ):
	return strings


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ "aba", "aa", "ad", "vcd", "aba" ] ), [ "aba", "vcd", "aba" ] )


	unittest.main()
