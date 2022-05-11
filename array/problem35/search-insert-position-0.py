from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        分为四种情况：
        1 target 最前
        2 target 最后
        3 target 在里面
        4 target 需要被介入
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle
        return right+1
