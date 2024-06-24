class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        list = []
        list2 = []
        cnt = 0
        dict = {}
        if len(nums) ==1:
            for i in range(1):
                nums[i] = str(nums[i])
            return nums
        else:
            for i in range(len(nums)):
                if list == [] or nums[i] - nums[i-1] == 1:
                    list.append(nums[i])
                    dict[cnt] = list
                else:
                    dict[cnt] = list
                    list = []
                    cnt += 1
                    list.append(nums[i])
                    dict[cnt] = list

            for i in dict:
                if min(dict[i]) == max(dict[i]):
                    a = str(min(dict[i]))
                else:
                    a = str(min(dict[i])) + '->' + str(max(dict[i]))
                list2.append(a)

            return list2