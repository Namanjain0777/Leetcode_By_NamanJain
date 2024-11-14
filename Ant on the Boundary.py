class Solution:
    def returnToBoundaryCount(self, nums):
        l = len(nums)
        a = 0
        count = 0
        i = 0
        while i < l:
            a += nums[i]
            if a == 0:
                count += 1
            i += 1
        return count
