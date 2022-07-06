class Solution:
	def maxSubArray( self, param1, ):
		return solution( param1 )


def solution( nums ):
	maxSum, *rest = nums
	track = [ maxSum ]
	for i , num in enumerate( rest ):
		prev_best = track[i]
		new_best = max( num , prev_best + num)
		track.append( new_best )

	return max( track )


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			nums = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
			self.assertEquals( solution( nums ), 6 )

		def test2( self ):
			nums = [ 1 ]
			self.assertEquals( solution( nums ), 1 )


	unittest.main()
