class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        nn = len(nums)/3
        dicc = {}
        for a in nums:
            try:
                dicc[a]+=1
            except:
                dicc[a]=1
        arr = []
        for a in dicc:
            if dicc[a]>nn:
                arr.append(a)
        return arr