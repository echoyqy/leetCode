def threeSum(nums: list):
    ans = []
    if len(nums) < 3:
        return []
    else:
        nums.sort()
        n = len(nums)
        for i in range(n):
            target = nums[i]
            # 需要和上一次枚举的数不相同
            if i > 0 and nums[i] == nums[i- 1]:
                continue
            third = n - 1
            for second in range(i + 1, n):
                if second > i + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] + target > 0:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] + target == 0:
                    ans.append([target, nums[second], nums[third]])
        return ans


if __name__ == '__main__':
    nums = [0, 0, 0]
    print(threeSum(nums))
