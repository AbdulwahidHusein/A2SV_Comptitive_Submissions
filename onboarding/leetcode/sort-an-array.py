class Solution:
    def merged(self, left_arr, right_arr):
        n1 = len(left_arr)
        n2 = len(right_arr)
        ptr1 = ptr2 = 0
        res = []
        while ptr1 < n1 and ptr2 < n2:
            if left_arr[ptr1]  <= right_arr[ptr2]:
                res.append(left_arr[ptr1])
                ptr1 += 1
            else:
                res.append(right_arr[ptr2])
                ptr2 += 1
        res.extend(left_arr[ptr1:])
        res.extend(right_arr[ptr2:])
        return res 
    def merge_sort(self, arr, left, right):
        if left == right:
            return [arr[left]]

        mid = left + (right - left) // 2
        left_sub = self.merge_sort(arr, left, mid)
        right_sub = self.merge_sort(arr, mid+1, right)
        return self.merged(left_sub, right_sub)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums, 0, len(nums)-1)