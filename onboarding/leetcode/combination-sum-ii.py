class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = Counter(candidates)
        s = set()
        uniques = list(set(candidates))
        n = len(uniques)
        def dfs(curr, _sum, start):
            nonlocal s , n
            if _sum == target:
                t = tuple(sorted(curr))
                s.add(t)
                return
            if _sum > target:
                return
            for i in range(start, n):
                if _sum + uniques[i] <= target:
                    curr.append(uniques[i])
                    _sum += uniques[i]
                    if c[uniques[i]] > 1:
                        c[uniques[i]] -= 1
                        dfs(curr, _sum, i)
                        c[uniques[i]] += 1
                    else:
                        dfs(curr, _sum, i+1)
                    curr.pop()
                    _sum -= uniques[i]
        dfs([], 0, 0)
        return [list(a) for a in s]
