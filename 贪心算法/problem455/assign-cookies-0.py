class Solution:
    def findContentChildren(self, g: list, s: list):
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i, j, count = 0, 0, 0
        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            j += 1
            i += 1
        return count


if __name__ == '__main__':
    solutioner = Solution()
    testValue = solutioner.findContentChildren(g=[1, 2, 3], s=[1, 2])
    print(testValue)
