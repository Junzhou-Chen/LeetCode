class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        begin = 0
        max_len = 1
        strs = s[begin:begin+1]
        for i in range(1,len(s)):
            str_i = s[i]
            while str_i in strs:
                begin += 1
                strs = s[begin:i]
            strs = s[begin:i+1]
            max_len = max(max_len, len(strs))
        return max_len