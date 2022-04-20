def solution( param1, param2 ):
	return param1


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 6 , 2 , 3 , 8 ] ) , 3 )


	unittest.main()
