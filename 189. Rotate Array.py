nums = [1,2,3,4,5,6,7]
k = 3

k = k % len(nums)      
# Get the number of elements to move from the end to the beginning
r = len(nums) - k
new = nums[0:r]
nums[0:r] = []
nums.extend(new)
print(nums)