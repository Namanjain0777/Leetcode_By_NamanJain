class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [n for n in nums if n > 0]
        nums.sort()

        target = 1
        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                return target
        
        return target
        
