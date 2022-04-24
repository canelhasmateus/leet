def solution( param1, param2 ):
	return []


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [25, 2 , 3 , 57 , 38 , 41]) , [ 2 , 3 ,5] )


	unittest.main()
