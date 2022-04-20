def solution( matrix ):
	haunted = set()
	res = 0

	for i, row in enumerate( matrix ):
		for j, cost in enumerate( row ):

			if cost == 0:
				haunted.add( j )

			if j not in haunted:
				res += cost

	return res


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			matrix = [ [ 0, 1, 1, 2 ],
			           [ 0, 5, 0, 0 ],
			           [ 2, 0, 3, 3 ] ]

			self.assertEquals( solution( matrix ), 9 )
		def test1( self ):
			matrix = [[1, 1, 1, 0],
			          [0, 5, 0, 1],
			          [2, 1, 3, 10]]

			self.assertEquals( solution( matrix ), 8 )


	unittest.main()
