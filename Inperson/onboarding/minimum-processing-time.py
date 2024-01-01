class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        n = len(processorTime)
        ans = 0
        j = 0
        for i in range(n):
            ans = max(ans, processorTime[i] + max(tasks[j: j+4]))
            j += 4
        return ans