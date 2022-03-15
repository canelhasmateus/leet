# Given n non-negative integers a1, a2, ..., an , 
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that
#  the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, 
# such that the container contains the most water.

# Notice that you may not slant the container.



# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
# Example 3:

# Input: height = [4,3,2,1,4]
# Output: 16
# Example 4:

# Input: height = [1,2,1]
# Output: 2


# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

using Test

function area((a, b), (c, d))
    height = min(b, d)
    return (c - a) * height
end

function biggestContainer(heights)
    left = 1
    right = length(heights)
    max_area = 0

    while left <= right
        new_area = area((left, heights[left]), (right, heights[right]))
        if new_area > max_area
            max_area = new_area
        end

        if heights[left] < heights[right]
            left += 1
        else
            right -= 1
        end

    end

    return max_area
end

@test biggestContainer([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
@test biggestContainer([1, 1]) == 1
@test biggestContainer([4, 3, 2, 1, 4]) == 16
@test biggestContainer([1, 2, 1]) == 2

