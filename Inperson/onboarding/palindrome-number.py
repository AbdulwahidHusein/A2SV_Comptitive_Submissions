class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        rv = ''
        st =str(x)
        for i in range(len(str(x))-1, -1, -1):
            rv += st[i]
        return rv==st
        