def solution( param1, param2 ):

	count = 0
	for left , right in zip( param1 , param2):
		if left == right:
			count+=1

	return count


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "aabcc", "adcaa" ), 3 )


	unittest.main()
