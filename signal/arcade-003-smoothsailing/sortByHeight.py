def solution( param1 ):
	people = [ ]
	trees = [ ]

	for i, value in enumerate( param1 ):

		if value == -1:
			trees.append( i )
		else:
			people.append( value )

	people = [ i for i in sorted( people ) ]
	for position in trees:
		people.insert( position, -1 )

	return people


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution(
				[ -1, 150, 190, 170, -1, -1, 160, 180 ] ),
				[ -1, 150, 160, 170, -1, -1, 180, 190 ] )


	unittest.main()
