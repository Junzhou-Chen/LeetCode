class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        cop = x
        while x != 0:
            res = res * 10 + x % 10
            x = x // 10
        # print(res)
        return res == cop