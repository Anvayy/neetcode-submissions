class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''.join(char for char in s if char.isalnum())
        strs = strs.lower()
        return True if strs == strs[::-1] else False
        