def solution( param1):
	return 0



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			matrix = [[0, 1, 1, 2],
			          [0, 5, 0, 0],
			          [2, 0, 3, 3]]

			self.assertEquals( solution( matrix) ,  9)


	unittest.main()
