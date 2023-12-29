from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda x: str(x)*10, reverse=True)
        
        string = ''.join(str(num) for num in nums)
        if int(string[0]) == 0:
            return '0'
        return string