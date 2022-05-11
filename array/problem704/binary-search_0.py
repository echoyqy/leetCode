from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        使用2分法进行数组的查找
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle
        return -1
