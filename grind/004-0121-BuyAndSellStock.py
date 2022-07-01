class Solution:
	def maxProfit( self, param1, ):
		return solution( param1, )

def solution( param1,  ):
	maxProfit = 0
	lowest_price , *rest = param1
	for price in rest:
		lowest_price = min( lowest_price , price)
		profit = price - lowest_price
		maxProfit = max( maxProfit , profit )


	return maxProfit






if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 7, 1, 5, 3, 6, 4 ] ), 5 )
		def test2( self ):
			self.assertEquals( solution( [7,6,4,3,1] ), 0 )


	unittest.main()
