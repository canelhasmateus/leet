# Given a string s, find the length of the longest substring without repeating characters.



# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

using Test


function substring(s::String)::Int64

    maximum_length = 0
    visited::Dict = Dict()
    left = right = 1

    while right <= length(s)
        rightChar = s[right]
        visited[rightChar] = get(visited, rightChar, 0) + 1

        while visited[rightChar] > 1
            leftChar = s[left]
            visited[leftChar] = get(visited, leftChar, 0) - 1
            left += 1
        end
        
        maximum_length = max(maximum_length, right - left + 1)
        right += 1
    end


    return maximum_length


end


@test substring("") == 0
@test substring("abcabcbb") == 3
@test substring("bbbbb") == 1
@test substring("pwwkew") == 3
