# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        oddpf = [0]
        evenpf = [0]
        for i in range(n-1, -1, -1):
            if i%2 == 0:
                evenpf.append(evenpf[-1] + nums[i])
                oddpf.append(oddpf[-1])
            else: 
                oddpf.append(oddpf[-1] + nums[i])
                evenpf.append(evenpf[-1])
        es, os = 0,0
        ans = 0
        oddpf.reverse()
        evenpf.reverse()
        for i in range(n):
            if os + evenpf[i+1] == es + oddpf[i+1]: 
                ans += 1
            if  i %2 == 0:
                es += nums[i]
            else:
                os += nums[i]
        return ans