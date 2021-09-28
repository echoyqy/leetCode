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
            result = []
            queue = collections.deque([root])
            while queue:
                level = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    queue.extend(node.children)
                result.append(level)
        return result

if __name__ == '__main__':
    solution = Solution()
    root = [1,None, 3, 2, 4, None, 5, 6]
    print(solution.levelOrder(root))




