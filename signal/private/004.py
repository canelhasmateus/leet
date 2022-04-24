def solution( words ):
	count = 0

	words = [ i for i in sorted( words ) ]

	for i in range( len( words ) - 1 ):
		for j in range( i + 1, len( words ) ):
			if words[ j ].startswith( words[ i ] ):
				count += 1
			else:
				break

	return count

if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			strings = [ "back", "backdoor", "gammon", "backgammon", "comeback", "come", "door" ]
			self.assertEquals( solution( strings ), 3 )


	unittest.main()
