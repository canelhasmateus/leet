class TreeNode:
	def __init__( self, val = 0, left = None, right = None ):
		self.val = val
		self.left = left
		self.right = right




class Solution:
	def invertTree( self, param1: TreeNode | None ):
		return solution( param1, )


def solution( param1: TreeNode | None ):
	if param1:
		param1.left , param1.right = param1.right, param1.left

		solution( param1.left )
		solution( param1.right )

	return param1



if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution(), True )


	unittest.main()
