def solution( operations ):
	...


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			operations = [ "TYPE Code", "TYPE Signal", "MOVE_CURSOR -3",
			               "SELECT 5 8", "TYPE ou", "UNDO", "TYPE nio" ],

			self.assertEquals( solution( operations), "CodeSignaliol" )


	unittest.main()
