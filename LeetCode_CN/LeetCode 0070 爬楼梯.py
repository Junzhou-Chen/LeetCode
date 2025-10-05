class Solution:
    def climbStairs(self, n: int) -> int:
        p,q,r = 0,0,1
        for i in range(n):
            p = q
            q = r
            r = q + p
        return r
# 看着这个easy我就特来气
