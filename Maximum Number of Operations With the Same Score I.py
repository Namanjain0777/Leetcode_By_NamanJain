class Solution:
    def maxOperations(self, nums) :
        c=nums[0]+nums[1]
        count=1
        i=2
        while i<=len(nums)-2:
            if nums[i]+nums[i+1]==c:
                count+=1
                i+=2
            else:
                break
        return count
                    
