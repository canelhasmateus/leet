def solution(yourLeft, yourRight, friendsLeft, friendsRight):
	yMax, yMin = max( yourLeft , yourRight) , min( yourLeft , yourRight)
	hMax, hMin = max( friendsLeft , friendsRight) , min( friendsLeft , friendsRight)



	return yMax == hMax and yMin == hMin


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( 10 , 15, 15 , 10), True )


	unittest.main()
