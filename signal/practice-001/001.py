

def solution( numbers ):

	res = []
	for i in range( len( numbers ) - 2 ):

		first, second, third = numbers[ i : i + 3 ]

		if first < second > third or first > second < third:
			z = 1
		else:
			z = 0

		res.append( z )

	return res


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 1, 2 , 1 , 3, 4] ), [1 , 1 ,0] )

		def test2( self ):
			self.assertEquals( solution( [ 1, 2 , 3, 4] ), [0 , 1] )


	unittest.main()
