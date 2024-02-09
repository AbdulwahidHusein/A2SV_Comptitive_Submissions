class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best_time = 0
        for customer in customers:
            best_time += customer == 'Y'
        
        ans, cur_time = 0, best_time
        for i, customer in enumerate(customers):
            if customer == 'Y':
                cur_time += -1
            else:
                cur_time += 1
            if cur_time < best_time:
                best_time = cur_time
                ans = i + 1

        return ans