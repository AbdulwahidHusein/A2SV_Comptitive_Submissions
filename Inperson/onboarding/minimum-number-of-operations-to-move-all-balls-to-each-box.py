class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        #lets brute force
        res = [0]*n
        for i in range(n):
            ans = 0
            for j in range(n):
                if boxes[j] == "1":
                    ans += abs(j-i)
            res[i] = ans
        return res

