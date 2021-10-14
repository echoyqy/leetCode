# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        else:
            minDepth = 10**6
            if  root.left:
                minDepth = min(self.minDepth(root.left), minDepth)
            if root.right:
                minDepth = min(self.minDepth(root.right), minDepth)
            return minDepth+1