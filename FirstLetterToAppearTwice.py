class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_set = set()
        for c in s:
            if c in s_set:
                return c            
            s_set.add(c)
