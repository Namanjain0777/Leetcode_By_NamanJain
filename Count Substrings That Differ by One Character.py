class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        result = 0
        
        for i in range(m):
            for j in range(n):
                k = 0
                mismatch = 0
                while i + k < m and j + k < n:
                    if s[i + k] != t[j + k]:
                        mismatch += 1
                    if mismatch == 1:
                        result += 1
                    elif mismatch > 1:
                        break
                    k += 1
        
        return result
