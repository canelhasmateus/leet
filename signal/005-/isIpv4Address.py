import re

pattern = re.compile("(\d{1,3})\.(\d{1,3})\.(\d{1,3})")
def solution( param1):
	match = pattern.match( param1)
	if match:
		for digits in match.groups():
			if int(digits) > 255:
				return False
		return True
	return False



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "172.16.254.1"), True )

		def test1( self ):
			self.assertEquals( solution( "172.316.254.1"), False )


	unittest.main()
