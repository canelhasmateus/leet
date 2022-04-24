def solution( message ):

	vowels = {"a", "e", "i", "o", "u"}
	res = []

	lastVowel = None
	firstVowel = 0

	for i , c in enumerate( message ):

		if c in vowels:
			if lastVowel:
				res.append( lastVowel)
			else:
				firstVowel = i
			lastVowel = c
		else:
			res.append( c )


	if lastVowel:
		res.insert( firstVowel , lastVowel)
	return "".join( res)


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "codesignal") , "cadosegnil")
		def test2( self ):
			self.assertEquals( solution( "plain text") , "plean tixt")
		def test3( self ):
			self.assertEquals( solution( "some message with punctuation marks, e.g. commas, dots, etc.")
			                   , "semo messega weth pinctuutain morks, a.g. cemmos, dats, otc.")


	unittest.main()
