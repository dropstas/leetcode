from typing import List

def removeElement(nums: List[int], val: int) -> int:
    cnt = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[cnt] = nums[i]
            cnt +=1
    return cnt

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))