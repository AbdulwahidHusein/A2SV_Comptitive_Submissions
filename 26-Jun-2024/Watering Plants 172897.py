# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # 3, 4, 5, 6f       6 + 8 + 10 + 6
        # 2, 3 4f         4 + 6 + 4  
        turning_pts = []
        curr_sum = 0
        ans = 0
        plants.append(0)
        n = len(plants)
        for i in range(n-1):
            curr_sum += plants[i]
            if curr_sum + plants[i+1] > capacity:
                turning_pts.append(i+1)
                curr_sum = 0
                

        #print(turning_pts)
        for i in range(len(turning_pts)):
            ans += 2*turning_pts[i]
        #ans += turning_pts[-1]
        return ans + n-1