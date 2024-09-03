class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""

        ans = strs[0]
        for i in range(len(ans)):
            for j in strs[1:]:
                if i==len(j) or j[i] != ans[i]:
                    return ans[0:i]

        return ans
        
