def solution( array, replaceable , replacement):

	res = []
	for element in array:

		if element == replaceable:
			res.append( replacement)
		else:
			res.append( element)

	return res

if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution([1,2,1] , 1 , 3), [3, 2, 3] )


	unittest.main()
