def solution( statues ):

	prev, *rest = sorted(statues)
	total = 0
	for current in rest:
		diff = current - prev
		total += diff - 1

		prev = current

	return total


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 6 , 2 , 3 , 8 ] ) , 3 )


	unittest.main()
