class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node'):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return res[::-1]



if __name__ == '__main__':
    souler = Solution()
    res = souler.postorder(root = Node([1,None,3,2,4,None,5,6]))
    print(res)