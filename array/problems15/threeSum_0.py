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
        if n < 3:
            return []
        else:
            for i in range(n):
                first = nums[i]
                others = nums[i + 1:]
                left, right = 0, len(others) - 1
                while left < right:
                    second = others[left]
                    third = others[right]
                    if second + third + first > 0:
                        right -= 1
                    elif second + third + first < 0:
                        left += 1
                    elif second + third + first == 0:
                        temp = [first, second, third]
                        if temp not in result:
                            result.append(temp)
                        right -= 1
                        left += 1
            return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solu = Solution()
    result = solu.threeSum(nums)
    print(result)
