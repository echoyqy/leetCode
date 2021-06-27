def removeDuplicates(nums):
    slow = fast = 1
    if not nums:
        return 0
    for fast in range(1, len(nums)):
        if fast > 0 and nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

if __name__ == '__main__':
    nums = [1, 1, 2]
    a = removeDuplicates(nums)
    print(a)
