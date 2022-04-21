def solution( param1, param2 ):

	counts = {}

	for left in param1:
		counts[ left ] = counts.get( left, 0 ) + 1

	total = 0
	for right in param2:
		current_count = counts.get( right, 0 )
		if current_count > 0:
			total += 1
			counts[ right ] = current_count - 1


	return total


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "aabcc", "adcaa" ), 3 )


	unittest.main()
