# Problem: Palindrome Number
# Approach: Reverse the number and compare it with the original.
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return original == reverse