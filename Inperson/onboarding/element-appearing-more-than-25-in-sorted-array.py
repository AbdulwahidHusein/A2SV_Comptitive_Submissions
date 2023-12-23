class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        l = len(arr)
        for n in arr:
            if 4*c[n] > l:
                return n