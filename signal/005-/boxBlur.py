def solution( photo ):
	return [[ ]]



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			image = [[1, 1, 1],
			         [1, 7, 1],
			         [1, 1, 1]]

			self.assertEquals( solution( image ) , [[ 1]] )


	unittest.main()
