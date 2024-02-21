class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greaters = {}
        for num in nums1:
            next_greaters[num] = -1

        for i in range(len(nums2)-1, -1, -1):
            while stack:
                val = stack[-1]
                if nums2[i] >= val:
                    stack.pop()
                else:
                    next_greaters[nums2[i]] = val
                    break
            stack.append(nums2[i])

        print(next_greaters)
        arr = []
        for num in next_greaters:
            if num in nums1:
                arr.append(next_greaters[num])
        return arr

                
