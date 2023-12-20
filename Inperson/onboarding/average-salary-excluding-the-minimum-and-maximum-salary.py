class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = float("inf")
        max_sal = -float("inf")
        n = len(salary)
        sal_sum = 0
        for s in salary:
            min_sal = min(min_sal, s)
            max_sal = max(max_sal, s)
            sal_sum += s

        return (sal_sum - min_sal - max_sal)/(n-2)