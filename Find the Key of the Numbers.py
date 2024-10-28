class Solution:
    def generateKey(self, num1, num2, num3):
        nums = [str(num1).zfill(4), str(num2).zfill(4), str(num3).zfill(4)]
        res = 0
        for i in range(4):
            c = min(nums[0][i], nums[1][i], nums[2][i])
            res = res * 10 + int(c)
        return res    
