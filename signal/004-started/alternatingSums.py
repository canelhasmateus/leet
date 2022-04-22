def solution2(a):

	return [sum(a[::2]),sum(a[1::2])]

def solution( param1):

	res = [ 0 , 0 ]
	for i, weight in enumerate(param1):
		idx = i % 2
		res[ idx ] = res[idx] + weight
	return res


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 50 , 60 , 60 , 45 , 70 ]), [ 180, 105] )


	unittest.main()
