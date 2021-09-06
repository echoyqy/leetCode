class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: TreeNode):
    def preorder(root: TreeNode):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    res = []
    preorder(root)
    return res

