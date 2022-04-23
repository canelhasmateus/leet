import re

pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}")
def solution( param1):
	if pattern.match( param1):

		return True
	return Falser



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "172.16.254.1"), True )


	unittest.main()
