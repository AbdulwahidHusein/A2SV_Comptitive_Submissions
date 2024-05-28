# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        start = 0
        end = 10**15
        lcm = math.lcm(divisor1, divisor2)
        def can_fill_with(n):
            available = n - (n // lcm)
            if available < uniqueCnt1 + uniqueCnt2:
                return False
            for1 = n - n // divisor1
            for2 = n - n // divisor2
            return for1 >= uniqueCnt1 and for2 >= uniqueCnt2 
        ans = 10**15
        while start <= end:
            mid = (start + end) // 2
            if can_fill_with(mid):
                ans = mid
                end = mid-1
            else:
                start = mid+1
        
        return ans