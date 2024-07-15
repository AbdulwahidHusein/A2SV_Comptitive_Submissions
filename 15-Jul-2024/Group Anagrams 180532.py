# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        strs.sort(key = lambda s: sorted(s))

        ans = []
        curr = [strs[0]]
        i = 1
        while i < n:
            if sorted(strs[i]) != sorted(strs[i-1]):
                ans.append(curr)
                curr = [strs[i]]
            else:
                curr.append(strs[i])
            i += 1
        ans.append(curr)
        
        return ans