class Solution:
    def rootToLeafPathSum(self, root, targetSum, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            sum += root.val
            if sum == targetSum:
                return True   
        return self.rootToLeafPathSum(root.left, targetSum, sum + root.val) or self.rootToLeafPathSum(root.right, targetSum, sum + root.val)

    def hasPathSum(self, root, targetSum) :
        sum = 0
        return self.rootToLeafPathSum(root, targetSum, sum)
