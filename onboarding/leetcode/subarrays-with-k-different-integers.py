class Solution:
    def atmostK(self,nums,k):
        curr=defaultdict(int)
        count = 0
        left = 0
        ans = 0
        for right in range(len(nums)):
            curr[nums[right]]+=1
            while(len(curr)>k):
                count+=1
                if nums[left] in curr:
                    curr[nums[left]]-=1
                    if curr[nums[left]]==0:
                        del curr[nums[left]]
                left+=1
            ans+=count
        return ans
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmostK(nums,k-1) - self.atmostK(nums,k)

