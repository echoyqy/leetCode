class Solution:
    def subsets(self, nums: list):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    def subsets2(self, nums):
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res

if __name__ == '__main__':
    solu = Solution()
    solu.subsets2([1, 2, 3])
