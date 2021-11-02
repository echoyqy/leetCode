class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickCom(N):
            if N == 0:
                return 1
            y = quickCom((N // 2))
            return y * y if N % 2 == 0 else y * y * x

        return quickCom(n) if n >= 0 else 1.0 / quickCom(-n)


if __name__ == '__main__':
    solu = Solution()
    y = solu.myPow(2, 2)
    print(y)
