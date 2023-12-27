class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c= Counter(arr1)
        n = len(arr1)
        ans = [0]*n
        ind = 0
        for i in range(len(arr2)):
            m = arr2[i]
            for j in range(c[m]):
                ans[ind] = m
                ind += 1
        rem = [j for j in arr1 if not j in arr2]
        rem.sort()
        for n in rem:
                ans[ind] = n
                ind += 1
        return ans