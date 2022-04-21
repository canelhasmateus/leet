def solution( param1, param2 ):


	counts = {}

	for left in param1:
		counts[left] = counts.get( left , 0) + 1

	for right in param2:
		counts[right] = max( counts.get( right , 0) - 1 , 0)


	total = 0
	for val in counts.values():
		total += val


	return len( param1 ) - total


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "aabcc", "adcaa" ), 3 )


	unittest.main()
