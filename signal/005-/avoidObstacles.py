def solution( obstacles ):
	i = 0
	while True:
		i += 1

		multiple = map( lambda x : x % i == 0, obstacles)

		if not any( multiple ):
			return i
	






if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 5, 3, 6, 7, 9 ] ), 4 )


	unittest.main()
