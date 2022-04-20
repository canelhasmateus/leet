def help( param1 , n ):
	head, *rest = param1

	if head and not rest:
		return n

	if head > rest[0]:
		n += 1

	return help( rest , n )


def solution( param1 ):
	n = help( param1 , 0)
	return n <= 1



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution([ 1, 3, 2,  1]), False )

		def test2( self ):
			self.assertEquals( solution([ 1, 3, 2 ]), True )


	unittest.main()
