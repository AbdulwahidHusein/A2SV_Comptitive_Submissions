from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.counter = defaultdict(int)
        self.frequency_counter = defaultdict(int)

    def add(self, number: int) -> None:
        self.frequency_counter[self.counter[number]] -= 1
        self.counter[number] += 1
        self.frequency_counter[self.counter[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.counter and self.counter[number] > 0:
            self.frequency_counter[self.counter[number]] -= 1
            self.counter[number] -= 1
            self.frequency_counter[self.counter[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency_counter[frequency] > 0