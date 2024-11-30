class Solution:
    def binary_search(self, nums, target, find_first):
        s = 0
        e = len(nums) - 1
        index = -1
        while s <= e:
            mid = s + (e - s) // 2
            if nums[mid] == target:
                index = mid
                if find_first:
                    e = mid - 1  # Find first occurrence
                else:
                    s = mid + 1  # Find last occurrence
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return index

    def searchRange(self, nums, target):
        first = self.binary_search(nums, target, True)
        last = self.binary_search(nums, target, False)
        return [first, last]
