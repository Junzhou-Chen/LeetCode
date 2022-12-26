class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(strs: str) -> int:
            return strs[::-1] == strs

        if not s: return ''
        res = s[0]
        for i in range(1,len(s)):
            # plural strs
            j = 0
            while i + j < len(s) and i - 1 - j >= 0:
                plural = s[i - j - 1: i + j + 1]
                if not isPalindrome(plural):
                    break
                else:
                    j += 1
                    if(len(res)<len(plural)): res = plural
            j = 1
            while i + j < len(s) and i - j >= 0:
                singular = s[i-j: i+j+1]
                if not isPalindrome(singular):
                    break
                else:
                    j+=1
                    if(len(res)<len(singular)): res = singular
        return res



        