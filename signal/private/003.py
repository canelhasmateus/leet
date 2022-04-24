def solution( matrix, framesize ):

	

	return 0



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			matrix = [[9,  7,  8,  9,  2],
			          [6,  9,  9,  6,  1],
			          [4,  10, 1,  3,  10],
			          [18,  2,  3,  9,  3],
			          [4,  6,  8,  5,  21]]

			self.assertEquals( solution(matrix,  3), 92 )


	unittest.main()
