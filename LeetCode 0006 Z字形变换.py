class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1:
            return s
        res_strs = [s[0]]
        s_size = len(s)
        for i in range(1,numRows):
            res_strs.append(s[i])
        num_place = numRows
        while num_place < s_size:
            for i in range(numRows - 2, -1, -1):
                if num_place == s_size: 
                    break
                res_strs[i] += s[num_place]
                num_place += 1
                
            for i in range(1, numRows):
                if num_place == s_size: 
                    break
                res_strs[i] += s[num_place]
                num_place += 1
                
        res = ''
        for i in range(numRows):
            res += res_strs[i]
        return res