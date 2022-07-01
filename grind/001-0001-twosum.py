class Solution:
	def twoSum( self, param1, param2 ):
		return solution( param1, param2 )


def solution( nums, target ):
	memo = { }
	for i, el in enumerate( nums ):


		remaining = target - el
		if remaining in memo:
			prev_seen = memo[ remaining ]
			return [ prev_seen, i ]

		memo[ el ] = i

if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution( [ 2, 7, 11, 15 ], 9 ), [ 0, 1 ] )

		def test1( self ):
			self.assertEquals( solution( [ 3 , 2, 4 ], 6 ), [ 1 , 2  ] )


	unittest.main()
