# Given a string s, return the longest palindromic substring in s.
# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"


# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


function palindrome(str)
    reverse(str) == str
end

function longestPalindrome(s)

    longest = ""
    for i = 1:length(s)
        for j = i:length(s)
            sub = s[i:j]
            if palindrome(sub) && length(sub) > length(longest)
                longest = sub
                break
            end

        end
    end

    return longest
end


using Test

@test longestPalindrome("babad") in ["bab", "aba"]
@test longestPalindrome("cbbd") == "bb"
@test longestPalindrome("a") == "a"
@test longestPalindrome("ac") == "a"

