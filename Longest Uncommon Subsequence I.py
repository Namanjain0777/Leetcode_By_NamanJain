class Solution(object):
    
    def findLUSlength(self,a,b) :
        # Check if both strings are equal
        if a == b:
            return -1
        else:
            # Return the length of the longest string between a and b
            return max(len(a), len(b))
