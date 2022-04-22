def solution( param1 ):

	prev, *rest = param1
	running_error = 0
	for current in rest:
		if current <= prev:
			diff = abs( current - prev )
			running_error += running_error + diff + 1

		prev = current
	return running_error


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 1, 1, 1 ] ), 3 )

		def test2( self ):
			self.assertEquals( solution( [ -1000, 0, -2, 0 ] ), 5 )


	unittest.main()
