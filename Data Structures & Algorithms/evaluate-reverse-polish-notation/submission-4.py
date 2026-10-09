class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit():
                stack.append(tokens[i])
            if len(stack) >= 2 and not tokens[i].lstrip('-').isdigit():
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == '+':
                    res = b+a
                elif tokens[i] == '-':
                    res = b-a
                elif tokens[i] == '*':
                    res = b*a
                elif tokens[i] == '/':
                    res = b/a
                stack.append(res)

        return int(stack[-1])