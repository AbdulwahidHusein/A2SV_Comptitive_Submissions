class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.sort()
        modified = ''
        curr = 0
        for i in range(len(s)):
            if curr<len(spaces) and i == spaces[curr]:
                modified += ' '+s[i]
                curr += 1
            else:
                modified += s[i]

        return modified