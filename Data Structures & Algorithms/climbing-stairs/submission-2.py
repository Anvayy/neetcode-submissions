class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1, 2:2}

        def f(x):
            if x in cache:
                return cache[x]
            
            cache[x] = f(x-1) + f(x-2)
            return cache[x]

        return f(n)