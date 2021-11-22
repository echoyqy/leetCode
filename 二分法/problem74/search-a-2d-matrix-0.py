#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 11:07
# @Author  : yangqy
# @Email   : yangqy@inhand.com.cn
# @Software: PyCharm


class Solution:
    def searchMatrix(self, matrix, target):
        line = len(matrix)
        rows = len(matrix[0])
        left = 0
        right = line * rows
        while left < right:
            i, j = divmod((left + right) // 2, rows)
            if matrix[i][j]== target:
                return True
            if matrix[i][j]<target:
                left = i*rows+j+1
            else:
                right = i*rows+j

        return False
