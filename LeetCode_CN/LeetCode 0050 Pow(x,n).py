class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if not N:
                return 1
            y = quickMul(N // 2)
            if N % 2:
                return y * y * x
            else:
                return y * y
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)