class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0]*1001

        for num_pass, start, end in trips:
            passengers[start] += num_pass
            passengers[end] -= num_pass
        
        for i in range(1, 1001):
            passengers[i] += passengers[i-1]
            if passengers[i] > capacity:
                return False
        if passengers[0] > capacity:
            return False
        
        return True