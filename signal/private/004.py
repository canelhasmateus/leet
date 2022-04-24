def solution( words ):
	count = 0

	for i in range( len( words ) - 1 ):
		for j in range( i + 1, len( words ) ):
			if words[ i ].startswith( words[ j ] ) or words[ j ].startswith( words[ i ] ):
				count += 1

	return count

if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			strings = [ "back", "backdoor", "gammon", "backgammon", "comeback", "come", "door" ]
			self.assertEquals( solution( strings ), 3 )


	unittest.main()
