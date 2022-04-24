def solution( numbers ):
	return []


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 1, 2 , 1 , 3, 4] ), [1 , 1 ,0] )


	unittest.main()
