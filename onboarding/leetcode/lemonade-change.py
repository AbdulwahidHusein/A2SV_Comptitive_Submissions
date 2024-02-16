class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fived = 0
        tend = 0
        for bill in bills:
            if bill == 5:
                fived += 5
            elif bill == 10:
                tend += 10
                if fived:
                    fived -= 5
                else:
                    return False
            elif bill == 20:
                if tend and fived:
                    fived -= 5
                    tend -= 10
                elif fived >= 15:
                    fived -= 15
                else:
                    return False

        return True