def solution( param1, param2 ):
	Lwrong = None
	Rwrong = None
	errors = 0
	for left, right in zip( param1, param2 ):
		if left != right:
			errors += 1
			if errors > 2:
				return False

			if Lwrong is None:
				Lwrong = left
				Rwrong = right
			else:
				if Rwrong != left or Lwrong != right:
					return False

	return True


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 1, 2, 3 ], [ 1, 2, 3 ] ), True )

		def test2( self ):
			self.assertEquals( solution( [ 1, 2, 3 ], [ 2, 1, 3 ] ), True )

		def test3( self ):
			self.assertEquals( solution( [ 1, 2, 2 ], [ 2, 1, 1 ] ), False )

		def test4( self ):
			self.assertEquals( solution( [ 1, 1, 4 ], [ 1, 2, 3 ] ), False )


	unittest.main()
