class Solution:
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxEnd = end + 1
            for i in range(start, end+1):
                if i+nums[i]>= n-1:
                    return step
                maxEnd = max(maxEnd, i+nums[i])
            start, end = end+1, maxEnd
        return step

