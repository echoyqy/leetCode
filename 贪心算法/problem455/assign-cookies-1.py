class Solution:
    def findContentChildren(self, g: list, s: list):
        g.sort()
        s.sort()
        m = len(g)
        n = len(s)
        i, j, count = 0, 0, 0
        while i < m and j < n:
            while i < m and g[i] > s[j]:
                i += 1
            if i < m:
                count += 1
            j += 1
            i += 1
        return count


if __name__ == '__main__':
    solutioner = Solution()
    testValue = solutioner.findContentChildren(g=[1, 2, 3], s=[1, 2])
    print(testValue)
