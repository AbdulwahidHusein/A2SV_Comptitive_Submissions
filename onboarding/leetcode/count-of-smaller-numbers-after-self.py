from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortl = SortedList()
        ans = []
        nums = nums[::-1]
        for n in nums:
            pos = bisect_left(sortl, n)
            ans.append(pos)
            sortl.add(n)
        return ans[::-1]