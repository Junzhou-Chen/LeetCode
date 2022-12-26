class Solution:
    def reverse(self, x: int) -> int:
        up_limit = 2**31
        do_limit = -2**31
        result = 0
        mid = 1
        if x < 0:
            mid = -1
            x = x * mid
        while x != 0:
            result = result * 10 + x % 10
            x = x // 10
        if result > up_limit or result < do_limit:
            return 0
        else:
            return result * mid