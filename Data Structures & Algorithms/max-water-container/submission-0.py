class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxwater = 0
        L = 0
        R = n-1 
        while L < R:
            w_cont = R-L
            h_cont = min(heights[L],heights[R])

            water = w_cont*h_cont
            maxwater = max(maxwater,water)
            if heights[L]>heights[R]:
                R -= 1
            elif heights[R]>heights[L]:
                L += 1
            else:
                L += 1
                R -= 1
        return maxwater
        