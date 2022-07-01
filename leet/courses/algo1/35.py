
class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:

		left, right = 0 , len( nums ) - 1

		while left <= right :

			pivot = left + ( right - left  ) // 2

			if nums[pivot] > target:
				right = pivot - 1
			elif nums[ pivot] < target:
				left = pivot + 1
			else:
				return pivot

		return left

