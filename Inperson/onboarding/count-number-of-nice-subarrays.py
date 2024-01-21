class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0
        j = 0
        temp = 0
        ans = 0
        while(j<len(nums)):

            if nums[j]%2!=0:
                temp+=1
                count = 0

            if temp==k:
                while(nums[i]%2==0):
                    count+=1
                    i+=1
                count+=1
                i+=1
                temp-=1
            
            ans +=count
            j+=1

        return ans