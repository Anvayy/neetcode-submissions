class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = {}
        s2freq = {}
        for i in s1:
            s1freq[i] = s1freq.get(i,0) + 1
        
        perm = len(s1)

        for R in range(len(s2)):
            s2freq[s2[R]] = s2freq.get(s2[R],0) + 1
            if R >= perm - 1:
                if s1freq == s2freq:
                    return True
                left_char = s2[R-perm+1]
                s2freq[left_char] -= 1

                if s2freq[left_char] == 0:
                    del s2freq[left_char]

        return False