def removeDuplicates(nums) -> int:
    if not nums:
        return 0
    else:
        fast= slow =1
        while fast<len(nums):
            if nums[fast]!=nums[fast-1]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
    return slow


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(removeDuplicates(nums))
