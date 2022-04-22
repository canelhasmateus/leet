def solution( param1 ):
	count = {}
	sum_oddness = 0
	for character in param1:
		new_count = count.get( character, 0 ) + 1
		count[ character ] = new_count
		sum_oddness += 	new_count % 2

	return sum( evens ) <= 1


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "aabb" ), True )


	unittest.main()
