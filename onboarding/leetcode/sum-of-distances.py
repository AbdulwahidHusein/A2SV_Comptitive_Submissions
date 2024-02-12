class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lcount =  defaultdict(list)
        ans = [0] * n
        for i in range(n):
            if nums[i] in lcount:
                ans[i] = i * lcount[nums[i]][0] - lcount[nums[i]][1]
            else:
                lcount[nums[i]] = [0, 0]
            lcount[nums[i]][0] += 1
            lcount[nums[i]][1] += i

        rcount =  defaultdict(list)
        for i in range(n-1, -1, -1):
            if nums[i] in rcount:
                ans[i] += rcount[nums[i]][1] - i * rcount[nums[i]][0]
            else:
                rcount[nums[i]] = [0, 0]
            rcount[nums[i]][0] += 1
            rcount[nums[i]][1] += i
        return ans