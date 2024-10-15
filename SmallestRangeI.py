class Solution(object):
    def smallestRangeI(self, nums, k):
        min_val = min(nums)
        max_val = max(nums)

        if (max_val - min_val) - (2 * k) <= 0 or max_val - min_val == 0:
            return 0
        else:
            return (max_val - min_val) - (2 * k)
