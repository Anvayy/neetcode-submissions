class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracks = { ')' : '(', ']' : '[', '}' : '{'}
        
        for ch in s:
            if ch in bracks:
                if stack and stack[-1] == bracks[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False
