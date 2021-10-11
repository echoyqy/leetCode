# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def tree(node):
            if not node:
                return
            tree(node.left)
            ls.append(node.val)
            tree(node.right)

        ls = []
        tree(root)
        for i in range(len(ls) - 1):
            if ls[i] >= ls[i + 1]:
                return False
        return True
