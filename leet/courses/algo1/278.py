# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def binarysearch( nums: List[ int ], target: int ) -> int:
	left, right = 0, len( nums ) - 1
	while left <= right:
		pivot = left + (right - left) // 2
		if nums[ pivot ] == target:
			return pivot
		if target < nums[ pivot ]:
			right = pivot - 1
		else:
			left = pivot + 1
	return -1

class Solution:

	def firstBadVersion(self, n: int) -> int:

		left , right = 1 , n

		while left <= right:
			pivot = ( right + left ) // 2
			if isBadVersion( pivot ):
				right = pivot - 1
			else:
				left = pivot + 1

		return left

