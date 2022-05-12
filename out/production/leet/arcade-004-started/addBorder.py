def solution( picture ):
	length = len( picture[ 0 ] ) + 2
	res = [ "*" * length  ]
	for element in picture:
		res.append( "*" + element + "*" )
	res.append("*" * length)
	return res


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ "abc", "ded" ] ), [ "*****",
			                                                   "*abc*",
			                                                   "*ded*",
			                                                   "*****" ] )


	unittest.main()
