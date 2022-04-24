def solution( words ):
	return 0


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			strings = ["back", "backdoor", "gammon", "backgammon", "comeback", "come", "door"]
			self.assertEquals( solution(strings), 3 )


	unittest.main()
