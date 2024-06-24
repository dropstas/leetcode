nums = [0,0,1,1,1,2,2,3,3,4]
nums1 = [0,0,0,0,0,0,0,0,0,0,0,0]
n = 0
cnt = 1


for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        nums[cnt] = nums[i]
        cnt += 1
        print(cnt)



