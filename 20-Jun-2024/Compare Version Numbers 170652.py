# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        for i in range(len(v1)):
            v1[i] = int(v1[i])
        for j in range(len(v2)):
            v2[j] = int(v2[j])
        

        v1.extend([0]* (len(v2) - len(v1)))
        v2.extend([0]* (len(v1) - len(v2)))

        i = 0
        while i < len(v1):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1
        return 0