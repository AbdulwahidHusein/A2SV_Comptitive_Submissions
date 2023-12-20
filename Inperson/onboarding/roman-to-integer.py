class Solution:
    def romanToInt(self, s: str) -> int:
        storeKeyValue = {}
        storeKeyValue['I'] = 1
        storeKeyValue['V'] = 5
        storeKeyValue['X'] = 10
        storeKeyValue['L'] = 50
        storeKeyValue['C'] = 100
        storeKeyValue['D'] = 500
        storeKeyValue['M'] = 1000
        s = s[::-1]
        integer = 0
        integer += storeKeyValue[s[0]]
        for i in range(1, len(s)):
            if storeKeyValue[s[i]] >= storeKeyValue[s[i-1]]:
                integer += storeKeyValue[s[i]]
            else:
                integer -= storeKeyValue[s[i]]
        return integer

        IIIVL