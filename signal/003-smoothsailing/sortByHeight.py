def solution( param1 ):
	return param1


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution(
				[ -1, 150, 190, 170, -1, -1, 160, 180 ] ),
				[ -1, 150, 160, 170, -1, -1, 180, 190 ] )


	unittest.main()
