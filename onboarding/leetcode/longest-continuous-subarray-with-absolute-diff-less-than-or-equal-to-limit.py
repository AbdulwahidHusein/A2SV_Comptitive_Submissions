class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 
        dec_queue = deque()
        inc_queue = deque()
        left = 0
        right = 1
        ans = 0
        dec_queue.append(nums[0])
        inc_queue.append(nums[0])
        while right < n:
            while  inc_queue and inc_queue[-1] > nums[right]:
                inc_queue.pop()
            while dec_queue and dec_queue[-1] < nums[right]:
                dec_queue.pop()
            inc_queue.append(nums[right])
            dec_queue.append(nums[right])

            if dec_queue[0] - inc_queue[0] > limit:
                if dec_queue[0] == nums[left]:
                    dec_queue.popleft()
                if inc_queue[0] == nums[left]:
                    inc_queue.popleft()
                left += 1
                
            ans = max(ans, right - left + 1)
            right += 1
        return ans
            
