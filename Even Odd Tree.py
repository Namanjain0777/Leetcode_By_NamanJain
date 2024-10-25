class Solution(object):
    def isEvenOddTree(self, root):
        que = [root]
        level = 0

        while len(que) > 0:
            prev = None
            for i in range(len(que)):
                node = que.pop(0)
                if level % 2 == 0:
                    if prev != None and node.val <= prev.val:
                        return False
                    if node.val % 2 == 0:
                        return False
                else:
                    if prev != None and node.val >= prev.val:
                        return False
                    if node.val % 2 != 0:
                        return False
                prev = node
                if node.left != None:
                    que.append(node.left)
                if node.right != None:
                    que.append(node.right)
            level += 1

        return True
        
