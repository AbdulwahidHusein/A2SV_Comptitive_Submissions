class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs[0])
        cols = len(strs)
        invalids = set()
        prev = "a"*rows
        for i in range(cols):
            curr = strs[i]
            for j in range(rows):
                if curr[j] < prev[j]:
                    invalids.add(j)
            prev = curr

        return len(invalids)