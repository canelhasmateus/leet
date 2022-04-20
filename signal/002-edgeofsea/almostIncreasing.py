def is_increasing( param1 ):
	if len( param1 ) <= 1:
		return True

	prev, *rest = param1
	for current in rest:
		if current <= prev:
			return False
		prev = current
	return True

def solution( param1 ):
	tmp = [ i for i in param1]
	for i in range(len(param1)):
		element = tmp.pop( i )
		if is_increasing( tmp ):
			return True

		tmp.insert( i , element)
	return False



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test0( self ):
			self.assertEquals( solution( [ 1 ] ), True )

		def test1( self ):
			self.assertEquals( solution( [ 1, 3, 2, 1 ] ), False )

		def test2( self ):
			self.assertEquals( solution( [ 1, 3, 2 ] ), True )

		def test3( self ):
			self.assertEquals( solution( [ 1, 2, 1, 2 ] ), False )

		def test4( self ):
			self.assertEquals( solution( [10, 1, 2, 3, 4, 5] ), True )


	unittest.main()
