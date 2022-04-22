def solution( param1, param2 ):
	if param1 == param2:
		return True

	difference = set( param1 ).difference( set( param2 ) )
	return len( difference ) == 0
	

if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 1, 2, 3 ], [ 1, 2, 3 ] ), True )

		def test2( self ):
			self.assertEquals( solution( [ 1, 2, 3 ], [ 2, 1, 3 ] ), True )


	unittest.main()
