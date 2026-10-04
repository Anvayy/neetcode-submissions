class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        L = 0
        max_length = 0
        
        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R],0) + 1
            while ((R-L+1) - max(freq.values())) > k:
                freq[s[L]] -= 1
                L += 1
            length = R-L+1
            max_length = max(max_length, length)
        
        return max_length
            
                    