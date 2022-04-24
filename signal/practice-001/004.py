def solution( numbers, k ):
	res = {}
	for i in range( len( numbers) ):
		remainder = i % k
		res[remainder] = res.get( remainder , 0) + 1


	count = 0
	for i , seen in res.items():

		if i == 0:
			count += seen * (seen - 1)
			res[i] = 0

		else:
			complement = k - i
			count += seen * res.get( complement , 0)
			res[i] = 0
			res[complement] = 0
	
	return count


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):

			self.assertEquals( solution(  [ 1 ,2 , 3 , 4 ,5] , 3 ) , 4 )


	unittest.main()