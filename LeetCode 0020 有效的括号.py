class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        return True if s == '' else False