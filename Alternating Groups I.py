class Solution:
    def numberOfAlternatingGroups(self, colors):
        res = 0
        n = len(colors)
        for i in range(n):
            pre = colors[i]
            cur = colors[(i + 1) % n]
            nxt = colors[(i + 2) % n]
            if pre != cur and cur != nxt:
                res += 1
        return res
