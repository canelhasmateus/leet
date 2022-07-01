class Solution:
	def isValid( self, param1, ):
		return solution( param1, )


def head( stack ):
	if stack:
		return stack[ -1 ]
	return None


def solution( word, ):
	pair = { '}': '{',
	         ')': '(',
	         ']': '[' }
	stack = [ ]
	for char in word:
		if char in {"{" , "(" , "["}:
			stack.append( char )
		else:
			if head( stack ) == pair[ char ]:
				stack.pop()
			else:
				return False

	return stack == [ ]


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "()" ), True )

		def test2( self ):
			self.assertEquals( solution( "()[]{}" ), True )

		def test3( self ):
			self.assertEquals( solution( "(]" ), False )

		def test4( self ):
			self.assertEquals( solution( "]" ), False )


	unittest.main()
