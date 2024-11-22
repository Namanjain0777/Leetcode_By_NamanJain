class Solution(object):
    def findDisappearedNumbers(self, nums):
        a = set(range(1,len(nums)+1))
        b = set(nums)
        return list(a-b)

