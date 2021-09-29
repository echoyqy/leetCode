import collections


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):
        if root is None:
            return []
        ques = collections.deque(root)
        level = []
        result = []
        while ques:
            level = []
            for i in range(len(ques)):
                node = ques.popleft()
                level.append(node.val)
                ques.extend(node.children)
            result.append(level)
        return result