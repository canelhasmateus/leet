def solution( param1 ):
	digits = str( param1 )
	size = len( digits )
	leftSum = 0
	rightSum = 0
	for i in range( size ):
		element = int( digits[ i ] )

		isLeft = (i < size / 2)

		if isLeft:
			leftSum += element
		else:
			rightSum += element


	return False


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( 1230 ), True )


	unittest.main()
