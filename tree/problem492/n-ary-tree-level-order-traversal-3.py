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
        else:
            queue = collections.deque([root])
            result = []
            while queue:
                level = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    queue.extend(node.children)
                result.append(level)
        return result