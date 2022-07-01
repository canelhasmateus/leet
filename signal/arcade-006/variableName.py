import re

allowed = re.compile("^[a-zA-Z_][a-zA-Z_0-9]{0,}$")
def solution( name ):
	if allowed.match( name ):
		return True
	return False

if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution("var_1__Int"), True )

		def test2( self ):
			self.assertEquals( solution("qq-q"), False )

		def test3( self ):
			self.assertEquals( solution("2w2"), False )

		def test4( self ):
			self.assertEquals( solution("a"), True )


	unittest.main()
