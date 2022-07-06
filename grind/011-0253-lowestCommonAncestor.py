from collections import deque


class Solution:
	def lowestCommonAncestor( self, root, p, q ):
		return solution( root, p, q )


def solution( root, p, q ):
	p, q = (p.val, q.val) if p.val <= q.val else (q.val, p.val)
	best = root
	todo = deque( [ root ] )
	while todo:
		current = todo.popleft()
		val = current.val
		if p <= q < val:
			todo.append( current.left )
		elif val < p <= q:
			todo.append( current.right )
		else:
			best = current
			break

	return best


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			self.assertEquals( solution(), True )


	unittest.main()
