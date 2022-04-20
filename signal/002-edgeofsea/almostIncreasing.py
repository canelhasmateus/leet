def solution( param1 ):
	head, *rest = param1

	if head and not rest:
		return True


	if head < rest[0] and solution( rest ) :
		return True

	return False


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution([ 1, 3, 2,  1]), False )


	unittest.main()
