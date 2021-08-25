# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        # 前序递归
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # # 中序递归
        return self.preorderTraversal(root.left)+[root.val]+self.preorderTraversal(root.right)


if __name__ == '__main__':

    s = Solution()
    root = TreeNode(left=1, right=2)
    a = s.preorderTraversal(root)
    print(a)
