def solution( numbers, k ):
	return 0


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):

			self.assertEquals( solution(  [ 1 ,2 , 3 , 4 ,5] , 3 ) , 4 )


	unittest.main()