def solution( param1 ):
	rev = param1[ ::-1 ]
	return param1 == rev


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertTrue( solution( "aabaa" ) )

		def test2( self ):
			self.assertFalse( solution( "abac" ) )

		def test3( self ):
			self.assertTrue( solution( "a" ) )


	unittest.main()
