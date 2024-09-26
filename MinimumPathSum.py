class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        t = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(grid, m - 1, n - 1, t)

    def solve(self,arr,m,n,t):
        if m == 0 and n == 0:
            return arr[0][0]
        elif m < 0 or n < 0:
            return float("inf")
        if t[m][n] != -1:
            return t[m][n]

        from_top = self.solve(arr, m - 1, n, t)
        from_left = self.solve(arr, m, n - 1, t)

        if from_top != float("inf"):
            from_top += arr[m][n]
        if from_left != float("inf"):
            from_left += arr[m][n]

        t[m][n] = min(from_top, from_left)
        return t[m][n]
