class Solution:
    def canJump(self, nums: list) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


if __name__ == '__main__':
    solutioner = Solution()
    print(solutioner.canJump([2, 3, 1, 1, 4]))
