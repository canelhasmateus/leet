import copy
import math


def solution( mines ):
	res = [ ]
	for i in range( len( mines ) ):
		res.append( [ 0 for _ in range( len( mines[ 0 ] ) ) ] )

	for i in range( len( mines ) ):
		for j in range( len( mines[ 0 ] ) ):
			if mines[ i ][ j ]:
				res[ i ][ j ] += 1
				res[ i ][ j + 1 ] += 1
				res[ i ][ j - 1 ] += 1
				res[ i + 1 ][ j ] += 1
				res[ i + 1 ][ j + 1 ] += 1
				res[ i + 1 ][ j - 1 ] += 1
				res[ i - 1 ][ j ] += 1
				res[ i - 1 ][ j + 1 ] += 1
				res[ i - 1 ][ j - 1 ] += 1

	return res


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			image = [ [ 1, 1, 1 ],
			          [ 1, 7, 1 ],
			          [ 1, 1, 1 ] ]

			self.assertEquals( solution( image ), [ [ 1 ] ] )

		def test2( self ):
			image = [ [ 7, 4, 0, 1 ],
			          [ 5, 6, 2, 2 ],
			          [ 6, 10, 7, 8 ],
			          [ 1, 4, 2, 0 ] ]

			self.assertEquals( solution( image ), [ [ 5, 4 ],
			                                        [ 4, 4 ] ] )


	unittest.main()

if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			matrix = [ [ True, False, False ],
			           [ False, True, False ],
			           [ False, False, False ] ]

			self.assertEquals( solution( matrix ), [ [ 1, 2, 1 ],
			                                         [ 2, 1, 1 ],
			                                         [ 1, 1, 1 ] ] )


	unittest.main()
