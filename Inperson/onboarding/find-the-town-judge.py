class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == [] and  n == 1:
            return 1
        trusted_c = defaultdict(int)
        trusts_c = defaultdict(int)

        for a, b in trust:
            trusts_c[a] += 1
            trusted_c[b] += 1
        
        for m in trusted_c:
            if trusted_c[m] == n-1 and trusts_c[m] == 0:
                return m
        return -1