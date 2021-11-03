class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quick_com(N):
            if N == 0:
                return 1
            y = quick_com(N // 2)
            if N % 2 == 0:
                return y * y
            else:
                return y * x * y

        return quick_com(n) if n >= 0 else 1 / quick_com(-n)
