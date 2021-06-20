class Solution:
    """
    思路：
    取第一个元素，然后做2数之和
    缺陷：
    时间复杂度和空间复杂度太高了
    """

    def threeSum(self, nums: list):
        nums.sort()
        n = len(nums)
        result = []
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = nums[first]
            third = n - 1
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] + target == 0:
                    result.append([target, nums[second], nums[third]])
        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solu = Solution()
    result = solu.threeSum(nums)
    print(result)
