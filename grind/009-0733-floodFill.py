from collections import deque


class Solution:
	def floodFill( self, image, sr, sc, color, ):
		return solution( image, sr, sc, color )


def solution( image, sr, sc, wantedColor, maxDepth = float( "inf") ):
	queue = deque( [ (0, sr, sc) ] )
	groupColor = image[ sr ][ sc ]
	nRows = len( image )
	nCols = len( image[ 0 ] )
	while queue:
		(depth, x, y) = queue.popleft()
		if (depth <= maxDepth and 0 <= x < nRows and 0 <= y < nCols):

			currentColor = image[ x ][ y ]
			if currentColor == groupColor and currentColor != wantedColor:
				image[ x ][ y ] = wantedColor

				newDepth = depth + 1
				queue.append( (newDepth, x + 1, y) )
				queue.append( (newDepth, x - 1, y) )
				queue.append( (newDepth, x, y + 1) )
				queue.append( (newDepth, x, y - 1) )

	return image


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ [ 0, 0, 0 ],
			                               [ 0, 0, 0 ] ], 0, 0, 0 ),
			                   [ [ 0, 0, 0 ],
			                     [ 0, 0, 0 ] ] )

		def test2( self ):
			self.assertEquals( solution( [ [ 1, 1, 1 ],
			                               [ 1, 1, 0 ],
			                               [ 1, 0, 1 ] ], 1, 1, 2 ),
			                   [ [ 2, 2, 2 ],
			                     [ 2, 2, 0 ],
			                     [ 2, 0, 1 ] ] )

		def test3( self ):
			self.assertEquals( solution( [ [ 0, 0, 0 ],
			                               [ 0, 0, 0 ] ], 1, 0, 2 ),
			                   [ [ 2, 2, 2 ],
			                     [ 2, 2, 2 ] ] )


	unittest.main()
