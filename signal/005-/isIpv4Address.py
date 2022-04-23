import re


def solution( param1 ):
	digits = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
	digits = { str( i ) for i in digits }

	splits = param1.split( "." )
	if len( splits ) != 4:
		return False

	for group in splits:
		if len( group) == 0:
			return False
		for i , character in enumerate( group ):
			if character not in digits:
				return False

			if character == "0" and i == 0:
				if len( group ) > 1:
					return False

		number = int(group)
		if number < 0 or number > 255:
			return False

	return True




	match = pattern.match( param1 )
	if match:
		for digits in match.groups():
			if 0 <= int( digits ) > 255:
				return False
		return True
	return False


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "172.16.254.1" ), True )

		def test2( self ):
			self.assertEquals( solution( "172.316.254.1" ), False )

		def test3( self ):
			self.assertEquals( solution( ".254.255.0" ), False )

		def test4( self ):
			self.assertEquals( solution( "1.1.1.1a" ), False )


	unittest.main()
