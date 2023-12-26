class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ''.join([str(dg) for dg in digits])
        n = int(st)+1
        s = str(n)
        digits = [int(b) for b in s]
        return digits