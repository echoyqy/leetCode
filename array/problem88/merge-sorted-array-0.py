def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    k = m + n -1
    while n >0 and m>0:
        if nums1[m-1]>nums2[n-1]:
            nums1[k] = nums1[m-1]
            m-=1
        else:
            nums1[k] = nums2[n-1]
            n-=1
        k-=1
    nums1[:n]=nums2[:n]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    a= merge(nums1, m, nums2, n)
    print(a)
    # 输出：[1, 2, 2, 3, 5, 6]

