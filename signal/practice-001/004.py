def solution( numbers, k ):
	count = 0
	for i in range( len( numbers)  - 1):
		for j in range( i + 1,  len(numbers)):

			if (numbers[i] + numbers[j]) % k == 0:
				count += 1
	return count


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):

			self.assertEquals( solution(  [ 1 ,2 , 3 , 4 ,5] , 3 ) , 4 )


	unittest.main()