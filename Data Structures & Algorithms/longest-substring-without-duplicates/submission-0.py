class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        left = 0
        

        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(s[i])
            length = i-left+1
            max_length = max(max_length, length)

        return max_length