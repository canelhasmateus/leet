def solution( param1):
	return ""


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "(bar)" ), "rab" )


	unittest.main()
