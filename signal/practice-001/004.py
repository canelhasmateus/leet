def solution( numbers, k ):
	res = {}
	count = 0
	for i in range( len( numbers) ):
		remainder = i % k
		complement = k - remainder

		complements = res.get( complement , 0)
		count += complements

		res[remainder] = res.get( remainder , 0) + 1


	return count


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution(  [ 1 ,2 , 3 , 4 ,5] , 3 ) , 4 )
		def test2( self ):
			self.assertEquals( solution(  [ 1 ,2 , 3 , 4 ,5 , 6 , 7 , 8 , 9 , 10] , 5 ) , 9 )


	unittest.main()