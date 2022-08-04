class Solution:
	def isBalanced(self, root):
		return solution( root )



memo = { }
def height(current):
	if not current:
		return 0

	if current in memo:
		return memo[ current ]

	leftSize = height( current.left )
	rightSize = height( current.right )
	size_ = 1 + max( leftSize, rightSize )

	memo[ current ]	 = size_
	return size_


def solution(root):
	todos = [ root ]

	while todos:
		current = todos.pop()
		if not current:
			continue

		diff = abs( height( current.left ) - height( current.right ) )

		if diff > 1:
			return False
		
		todos.append( current.left )
		todos.append( current.right )

	return True


