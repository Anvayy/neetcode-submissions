class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        for i in t:
            t_freq[i] = t_freq.get(i,0) + 1
        
        need = len(t_freq)
        have = 0

        min_string = ""
        s_freq = {}
        L = 0

        for R in range(len(s)):
            s_freq[s[R]] = s_freq.get(s[R],0) + 1
            if s[R] in t_freq and s_freq[s[R]] == t_freq[s[R]]:
                have += 1
            while have == need:
                if min_string == "" or len(s[L:R+1]) < len(min_string):
                    min_string = s[L:R+1]   
                s_freq[s[L]] -= 1
                if s[L] in t_freq and s_freq[s[L]] < t_freq[s[L]]:
                    have -= 1
                L += 1

        return min_string
            
