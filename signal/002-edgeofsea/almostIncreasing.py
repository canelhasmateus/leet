def help( param1 ):
	prev, *rest = param1
	prevDiff = 0
	errors = 0

	for current in rest:
		diff = current - prev

		if current > prev:
			prev = current
			prevDiff = diff
		else:
			errors += 1
			


		if errors > 1:
			return False

	return True


def solution( param1 ):
	return help( param1 )


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test0( self ):
			self.assertEquals( solution( [ 1 ] ), True )

		def test1( self ):
			self.assertEquals( solution( [ 1, 3, 2, 1 ] ), False )

		def test2( self ):
			self.assertEquals( solution( [ 1, 3, 2 ] ), True )

		def test3( self ):
			self.assertEquals( solution( [ 1, 2, 1, 2 ] ), False )


	unittest.main()
