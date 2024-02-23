class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant_bans = 0
        dire_bans = 0
        radiant_count = senate.count('R')
        dire_count = senate.count('D')

        while radiant_count > 0 and dire_count > 0:
            new_senate = []
            for senator in senate:
                if senator == 'R':
                    if radiant_bans > 0:
                        radiant_bans -= 1
                    else:
                        dire_bans += 1
                        new_senate.append("R")
                else:
                    if dire_bans > 0:
                        dire_bans -= 1
                    else:
                        radiant_bans += 1
                        new_senate.append("D")

            senate = new_senate
            radiant_count = senate.count('R')
            dire_count = senate.count('D')

        return "Radiant" if radiant_count > 0 else "Dire"