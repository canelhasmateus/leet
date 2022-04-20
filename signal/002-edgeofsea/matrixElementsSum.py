def solution( matrix):

	haunted = set()
	res = 0
	for (i , row) in enumerate( matrix ) :
		for ( j , col) in enumerate( row ):

			cost = matrix[i][j]
			if cost == 0:
				haunted.add( j )

			if j not in haunted:
				res += cost

	return res



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			matrix = [[0, 1, 1, 2],
			          [0, 5, 0, 0],
			          [2, 0, 3, 3]]

			self.assertEquals( solution( matrix) ,  9)


	unittest.main()
