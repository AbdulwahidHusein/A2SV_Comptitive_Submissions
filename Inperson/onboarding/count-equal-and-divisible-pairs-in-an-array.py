class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pos_holder = defaultdict(list)
        ans = 0
        for i, n in enumerate(nums):
            pos_holder[n].append(i)
        for n in pos_holder:
            indexes = pos_holder[n]
            for i in range(len(indexes)):
                for j in range(i+1, len(indexes)):
                    if (indexes[i]  * indexes[j] )%k == 0:
                        ans += 1
        return ans