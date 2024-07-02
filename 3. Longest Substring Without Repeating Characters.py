class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        nums = list(s)

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        l = 0
        r = 0

        long = 0

        while True:
            if r >= len(nums):
                break
            if nums[r] in nums[l:r]:
                l = l + nums[l:r].index(nums[r])+1
            r += 1
            if len(nums[l:r]) > long:
                long = len(nums[l:r])
        
        return long
            