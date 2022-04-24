def solution( words ):

	count = 0
	words = [ i for i in sorted( words )]

	# A prefix must come before when sorted.

	for i in range( len( words) - 1):

		word = words[i ]
		inc = 1

		while True:
			try :
				next = words[ i + inc]
			except:
				break

			if not next.startswith( word ):
				break
			else:
				count+=1
				inc += 1

	return count


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			strings = [ "back", "backdoor", "gammon", "backgammon", "comeback", "come", "door" ]
			self.assertEquals( solution( strings ), 3 )


	unittest.main()
