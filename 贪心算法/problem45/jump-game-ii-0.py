class Solution:
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        # 进入查找循环
        while end < n - 1:
            step += 1
            maxEnd = end + 1
            for i in range(start, end + 1):
                # 判断是否可以到达
                if i + nums[i] >= n + 1:
                    return step
                # 找到最远的点
                maxEnd = max(maxEnd, i + nums[i])
            # 更新下一次的起始点
            start, end = end + 1, maxEnd
        return step


if __name__ == '__main__':
    solutioner = Solution()
    print(solutioner.jump([2, 3, 1, 1, 4]))
