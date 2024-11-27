class Solution(object):
    def fourSum(self, nums, target):
        ans = []
        n = len(nums)

        nums.sort()

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                li, ri = j + 1, n - 1

                while li < ri:
                    total = nums[i] + nums[j] + nums[li] + nums[ri]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[li], nums[ri]])

                        li += 1
                        ri -= 1

                        while li < ri and nums[li] == nums[li - 1]:
                            li += 1
                        while li < ri and nums[ri] == nums[ri + 1]:
                            ri -= 1
                    elif total < target:
                        li += 1
                    else:
                        ri -= 1

        return ans
