class Solution:
    """双指针法
    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    @classmethod
    def removeElement(cls, nums: list, val: int) -> int:
        fast = slow = 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
