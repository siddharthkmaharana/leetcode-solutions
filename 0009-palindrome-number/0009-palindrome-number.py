class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes
        if x < 0:
            return False

        # Numbers ending in 0 cannot be palindromes
        # except 0 itself
        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Even digits: x == reversed_half
        # Odd digits:  x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10