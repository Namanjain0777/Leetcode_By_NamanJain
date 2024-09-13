class Solution:
    def generateParenthesis(self, n):
        res = []

        def dfs(oP, cP, s):
            if oP == cP and oP + cP == n * 2:
                res.append(s)
                return
            
            if oP < n:
                dfs(oP + 1, cP, s + "(")
            
            if cP < oP:
                dfs(oP, cP + 1, s + ")")

        dfs(0, 0, "")

        return res
