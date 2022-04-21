import re

pattern = re.compile( "\([a-zA-Z]+\)" )


def removeBrackets( arg ):
	return arg.replace( "(" , "" ).replace(")" , "")
def solution( param1 ):
	match = pattern.match( param1 )
	if match:
		return removeBrackets( match.group() )[::-1]


	return ""


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "(bar)" ), "rab" )


	unittest.main()
