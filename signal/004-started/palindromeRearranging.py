def solution( param1 ):
	count = {}
	for character in param1:
		count[ character ] = count.get( character , 0 ) + 1

	res = 0
	for value in count.values():
		res += value % 2

	return res <= 1


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "aabb" ), True )


	unittest.main()
