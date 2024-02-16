class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #n rabi=bits say n-1
        answers.sort()
        n = len(answers)
        rabbits = 0
        j = 0
        while j < n and answers[j] == 0:
            rabbits += 1
            j += 1
            if j == n:
                return rabbits

        start = answers[j]
        count = 1
        for i in range(j, n):
            if answers[i] > start or count > start + 1:
                rabbits += start + 1
                count = 1
                start = answers[i]
            count += 1
        rabbits += start + 1
        
        return rabbits 
