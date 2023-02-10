class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def appendParenthesis(strs,leftlen,rightlen,n):
            if leftlen == n and rightlen == n:
                ans.append(strs)
                return
            if leftlen < n:
                newstr = strs + "("
                appendParenthesis(newstr,leftlen+1,rightlen,n)
            if rightlen < n and rightlen < leftlen:
                newstr = strs + ")"
                appendParenthesis(newstr,leftlen,rightlen+1,n) 
        appendParenthesis("",0,0,n)
        return ans