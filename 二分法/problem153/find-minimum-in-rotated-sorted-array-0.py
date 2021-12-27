#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 11:17
# @Author  : yangqy
# @Email   : yangqy@inhand.com.cn
# @Software: PyCharm


class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
