class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = []
        even_sum = 0
        for m in nums:
            if m%2 == 0:
                even_sum += m

        for val, index in queries:
            c = nums[index]
            if c%2 == 0:#it is in evensum
                if val%2 == 0:
                    even_sum += val
                    ans.append(even_sum)
                else:
                    even_sum -= c
                    ans.append(even_sum)
            else:#it was not in evens
                if val % 2 != 0:
                    even_sum += (val + c)
                    ans.append(even_sum)
                else:
                    ans.append(even_sum)
            nums[index] += val
        return ans