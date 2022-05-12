import itertools


def solution( matrix ):
	res = [ ]
	height = len( matrix )
	length = len( matrix[ 0 ] )
	for i in range( height ):
		res.append( [ 0 for _ in range( length ) ] )

	for i in range( height ):
		for j in range( length ):
			if matrix[ i ][ j ]:
				for r, c in itertools.product( (-1, 0, 1), repeat=2 ):
					newI = i + r
					newJ = j + c

					if 0 <= newI < height and 0 <= newJ < length:
						res[ newI ][ newJ ] += 1
				res[ i ][ j ] -= 1

	return res


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
