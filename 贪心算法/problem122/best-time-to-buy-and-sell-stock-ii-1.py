class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(0, len(prices) - 1):
            tmp = prices[i + 1] - prices[i]
            if tmp > 0:
                profit += tmp
        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solutioner = Solution()
    result = solutioner.maxProfit(prices)
    print(result)
