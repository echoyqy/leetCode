#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 10:04
# @Author  : yangqy
# @Email   : yangqy@inhand.com.cn
# @Software: PyCharm


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
