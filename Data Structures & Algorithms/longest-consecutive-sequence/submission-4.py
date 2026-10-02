class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        longest = 1
        curr = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr += 1
                longest = max(curr,longest)
            elif nums[i] != nums[i-1]:
                curr = 1
            
        return longest


        