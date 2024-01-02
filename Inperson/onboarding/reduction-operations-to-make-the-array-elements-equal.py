class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        #5:3, 3:2, 2:1, 1:4
        oprs = 0
        c = Counter(nums)
        
        numset = list(set(nums))
        numset.sort(reverse = True)
        n = len(numset)

        for i in range(n-1):
            oprs += c[numset[i]]
            c[numset[i+1]] += c[numset[i]]
        return oprs