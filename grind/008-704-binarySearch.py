class Solution:
	def search( self, param1, param2 ):
		return solution( param1, param2 )


def solution( param1, target ):

	p , q = 0 , len( param1) - 1
	while p <= q:
		pivot = int( (p + q ) / 2 )
		el = param1[ pivot ]
		if el < target:
			p = pivot + 1
		elif el > target:
			q = pivot - 1
		elif el == target:
			return pivot

	return -1


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ -1, 0, 3, 5, 9, 12 ], 9 ), 4 )
		def test2( self ):
			self.assertEquals( solution( [ -1, 0, 3, 5, 9, 12 ], 2 ), -1)


	unittest.main()
