class Solution:
    def mySqrt(self, x: int):
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

if __name__ == '__main__':
    solutioner = Solution()
    print(solutioner.mySqrt(8))