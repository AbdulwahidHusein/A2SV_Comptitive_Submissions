class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0]*n

        for start, end, seats in bookings:
            flights[start-1] += seats
            if end < n:
                flights[end] -= seats
        for i in range(1, n):
            flights[i] += flights[i-1]
            
        return flights
