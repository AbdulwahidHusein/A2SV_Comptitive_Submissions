class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        pos = bisect_left(arr, x)
        if pos == n:
            return arr[-k:]
        if pos > 0 and abs(arr[pos]-x) >= abs(arr[pos-1] - x):
            pos -= 1
        ans = [arr[pos]]
        left = pos - 1
        right = pos + 1
        while len(ans) < k:
            num = 0
            if left == -1:
                num = arr[right]
                right += 1
            elif right == n:
                num = arr[left]
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right]-x):
                num = arr[left]
                left -= 1
            else:
                num = arr[right]
                right += 1
            ans.append(num)
        ans.sort()
        return ans
