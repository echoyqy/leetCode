class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        if n<3:
            return []
        nums.sort()
        else:
            for i in range(n):
                first =nums[i]
                if first<=0:
                    traget = -first
                    second = i+1
                    third = n
                    if third+second+traget==0:
                        result.appened([first, second, third])
                    if third+second+traget>0:

