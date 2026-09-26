class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            numb = target - num
            if numb in seen:
                return [seen[numb], i]
            seen[num]=i
