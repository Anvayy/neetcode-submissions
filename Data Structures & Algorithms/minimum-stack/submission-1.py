class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
        

    def push(self, val: int) -> None:
        if not self.min_stack:
            min_ele = val
        else:
            min_ele = min(self.min_stack[-1], val)

        self.min_stack.append(min_ele)

        return self.stack.append(val)

    def pop(self) -> None:
        ele = self.stack.pop()
        
        self.min_stack.pop()
        return ele

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
