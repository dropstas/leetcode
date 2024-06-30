class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_item = 0
        max = 0

        for i in set(nums):
            if nums.count(i) > max_item and nums.count(i) > len(nums) / 2:
                max = i
                max_item = nums.count(i)
            
        return max
