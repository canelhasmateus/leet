def zigzag( a , b , c ):
	if a < b > c or a > b < c:
		return 1
	return 0


def solution( numbers ):

	res = []
	for i in range( len( numbers ) - 2 ):

		first, second, third = numbers[ i : i + 3 ]
		z = zigzag( first , second , third)
		res.append( z )

	return res


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 1, 2 , 1 , 3, 4] ), [1 , 1 ,0] )


	unittest.main()
