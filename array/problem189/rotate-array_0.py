def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(nums, k))
