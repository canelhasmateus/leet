def solution2(inputString):

	return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

def solution( param1 ):
	count = {}
	for character in param1:
		count[ character ] = count.get( character, 0 ) + 1

	evens = map( lambda x: x % 2,
	             count.values() )

	return sum( evens ) <= 1


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( "aabb" ), True )


	import time

	start = time.time()
	for _ in range( 5000000 ):
		solution( "aabb" )
	elapsed = time.time() - start
	print( elapsed )

	start = time.time()
	for _ in range( 5000000 ):
		solution2( "aabb" )
	elapsed = time.time() - start
	print( elapsed )

	# unittest.main()
