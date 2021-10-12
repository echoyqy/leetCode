# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []

        def tree(root):
            if not root:
                return False
            tree(root.left)
            res.append(root.val)
            tree(root.right)

        tree(root)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True
