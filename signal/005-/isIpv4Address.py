import re


pattern = re.compile( "^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
                      "")
def solution( param1 ):

	match = pattern.match(param1)
	if not match:
		return False

	splits = match.groups()

	for g , group in enumerate( splits ):

		if len( group) == 0:
			return False

		for i , character in enumerate( group ):
			if character == "0" and i == 0:
				if len( group ) > 1:
					return False

		number = int(group)
		if number < 0 or number > 255:
			return False

	return True


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

		def test5( self ):
			self.assertEquals( solution( "0.254.255.0" ), True )


	unittest.main()
