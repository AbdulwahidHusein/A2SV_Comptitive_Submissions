class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs[0]=="":
            return ""
        st = strs[0]
        exist = True
        leng = len(st)
        for i in range(leng, 0, -1):
            strr = st[:i]
            exist = True
            for a in strs:
               
                if not a.startswith(strr):
                    exist = False
            if exist:
                return strr
            if i==1:
                return ''
