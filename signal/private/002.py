def solution( message ):

	res = []
	lastVowel = None
	firstVowel = 0
	for i , c in enumerate( message ):

		if c in { "a" , "e" , "i" , "o" , "u"}:
			if lastVowel:
				res.append( lastVowel)
			else:
				firstVowel = i
			lastVowel = c
		else:
			res.append( c )



	res.insert( firstVowel , lastVowel)
	return "".join( res)


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "codesignal") , "cadosegnil")
		def test2( self ):
			self.assertEquals( solution( "plain text") , "plean tixt")


	unittest.main()
