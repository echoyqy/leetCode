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
        minHeight = 10 ** 10
        if root.right:
            minHeight = min(self.minDepth(root.right), minHeight)
        if root.left:
            minHeight = min(self.minDepth(root.left), minHeight)
        return minHeight + 1
