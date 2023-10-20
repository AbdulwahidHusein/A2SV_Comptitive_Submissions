class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        boats = 0
        end = len(people) - 1
        start = 0
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
                end -= 1
            else:
                start += 1
            boats += 1
        return boats
        