class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        pos = bisect_left(arr, x)
        if pos == n:
            return arr[-k:]
        if pos > 0 and pos < n and abs(arr[pos]-x) >= abs(arr[pos-1] - x):
            pos -= 1
        ans = [arr[pos]]
        left = pos - 1
        right = pos + 1
        while len(ans) < k:
            if left == -1:
                ans.append(arr[right])
                right += 1
            elif right == n:
                ans.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right]-x):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
        ans.sort()
        return ans
