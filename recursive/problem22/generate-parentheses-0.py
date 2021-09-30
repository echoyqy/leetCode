class Solution:
    def generateParenthesis(self, n: int):

        if n <= 0:
            return []
        res = []

        def dfs(paths, left, right):
            if left > n or right > left:
                return
            if len(paths) == n*2:
                res.append(paths)
                return
            dfs(paths+'(', left+1, right)
            dfs(paths+')', left, right+1)
        dfs('', 0, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    a = s.generateParenthesis(3)
    print(a)
