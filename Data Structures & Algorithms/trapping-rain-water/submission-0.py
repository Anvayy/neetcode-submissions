class Solution:
    def trap(self, height: List[int]) -> int:
        max_L = [0]*len(height)
        max_R = [0]*len(height)

        max_l_w = 0
        max_r_w = 0
        for i in range(len(height)):
            if not max_L:
                max_L.append(height[i])
            else:
                max_l_w = max(height[i], max_l_w)
                max_L[i] = max_l_w
        
        for i in range(len(height)-1, -1, -1):
            if not max_R:
                max_R.append(height[i])
            else:
                max_r_w = max(height[i], max_r_w)
                max_R[i] = max_r_w

        res = []
        for i in range(len(height)):
            res.append(min(max_L[i], max_R[i]))

        water = []
        for i in range(len(height)):
            water.append(res[i]-height[i])
        
        return sum(water)


        