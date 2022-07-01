class Solution:
	def isAnagram( self, param1, param2 ):
		return solution( param1, param2 )


def solution( param1, param2 ):
	if len(param1) != len(param2):
		return not True

	letters = { }
	for char in param1:
		letters[ char ] = letters.get( char, 0 ) + 1

	for char in param2:
		try:
			letters[ char ] = letters[ char ] - 1

			if letters[ char ] == 0:
				del letters[ char ]

		except KeyError:
			return False

	return len( letters ) == 0


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "anagram", "nagaram" ), True )

		def test2( self ):
			self.assertEquals( solution( "cat", "rat" ), False )


	unittest.main()
