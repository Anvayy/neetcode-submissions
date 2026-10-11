class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        candidate = float('inf')
        key = nums[r]

        while l <= r:
            
            mid = (l+r)//2
            if nums[mid] > key:
                l = mid + 1
            elif nums[mid] <= key:
                candidate = min(nums[mid],candidate)
                r = mid - 1

        return candidate
