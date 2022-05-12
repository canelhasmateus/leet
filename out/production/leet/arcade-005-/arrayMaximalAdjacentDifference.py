import math


def solution( param1 ):

	prev, *rest = param1

	res = -math.inf
	for current in rest:
		diff = abs( prev - current)
		res = max( diff , res )

		prev = current

	return res


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution([2, 4, 1, 0]), 3 )


	unittest.main()
