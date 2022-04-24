def solution( numbers ):

	counts = {}
	for digits in map( str , numbers):
		for character in digits:
			counts[character] = counts.get( character , 0 ) + 1

	mx = max( counts.values() )
	res = [ int( k)  for k , v in counts.items() if v == mx ]
	return [ i for i in sorted( res ) ]


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [25, 2 , 3 , 57 , 38 , 41]) , [ 2 , 3 ,5] )


	unittest.main()
