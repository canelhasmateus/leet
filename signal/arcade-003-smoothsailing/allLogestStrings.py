def solution( strings ):
	longest = max( map( len, strings ) )

	return [ i for i in strings if len( i ) == longest ]


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ "aba", "aa", "ad", "vcd", "aba" ] ), [ "aba", "vcd", "aba" ] )


	unittest.main()
