class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        elif n >= 3:
            dp = [1, 2]
            for i in range(2, n):
                dp.append(dp[0] + dp[1])
                dp.pop(0)
            return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
