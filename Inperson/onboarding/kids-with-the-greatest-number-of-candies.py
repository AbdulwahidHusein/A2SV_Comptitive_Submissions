class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        n = len(candies)
        ans = [0]*(n)

        for i in range(n):
            if candies[i] + extraCandies >= largest:
                ans[i] = True
            else:
                ans[i] = False
        return ans