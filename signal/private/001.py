import math


def solution( numbers ):
	res = [ ]

	for i in range( len( numbers ) ):
		element = numbers[ i ]
		last = numbers[ i + 1 ] if  0 <= i + 1  < len( numbers ) else math.inf
		next = numbers[ i + 2 ] if  0 <= i + 2  < len( numbers ) else math.inf

		res.append( min( [ element, last, next ] ) )

	return res


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 0, 4, 3, 1, 2 ] ), [ 0, 1, 1, 1, 2 ] )


	unittest.main()
