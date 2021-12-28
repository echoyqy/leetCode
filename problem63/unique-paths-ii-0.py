#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 10:11
# @Author  : yangqy
# @Email   : yangqy@inhand.com.cn
# @Software: PyCharm

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:

        height, width = len(obstacleGrid), len(obstacleGrid[0])
        store = [[0] * width for i in range(height)]

        for m in range(height):
            for n in range(width):
                if not obstacleGrid[m][n]:
                    if m == 0 and n == 0:
                        store[m][n] = 1
                    else:
                        a = store[m - 1][n] if m != 0 else 0
                        b = store[m][n - 1] if n != 0 else 0
                        store[m][n] = a + b
        return store[-1][-1]


if __name__ == '__main__':
    soluter = Solution()
    print(soluter.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
