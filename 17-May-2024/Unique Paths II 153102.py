# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # Get the number of rows and columns in the obstacle grid
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        # Create a 2D array to store the number of ways to reach each grid
        nums_of_ways_ij = [[0 for _ in range(col)] for _ in range(row)]

        # If the starting grid is an obstacle, there is no way to reach the destination
        if obstacleGrid[0][0] == 1:
            return 0
            

        # Set the number of ways to reach the starting grid as 1
        nums_of_ways_ij[0][0] = 1

        # Calculate the number of ways to reach each grid in the first column
        for i in range(1, row):
            if obstacleGrid[i][0] == 1:
                nums_of_ways_ij[i][0] = 0  # If the current grid is an obstacle, set the number of ways as 0
            else:
                nums_of_ways_ij[i][0] = nums_of_ways_ij[i-1][0]  # Otherwise, use the number of ways from the previous grid

        # Calculate the number of ways to reach each grid in the first row
        for j in range(1, col):
            if obstacleGrid[0][j] == 1:
                nums_of_ways_ij[0][j] = 0  # If the current grid is an obstacle, set the number of ways as 0
            else:
                nums_of_ways_ij[0][j] = nums_of_ways_ij[0][j-1]  # Otherwise, use the number of ways from the previous grid

        # Calculate the number of ways to reach each grid in the remaining rows and columns
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    # If the current grid is not an obstacle, calculate the number of ways as the sum of
                    # the number of ways from the grid above and the number of ways from the grid on the left
                    nums_of_ways_ij[i][j] = nums_of_ways_ij[i-1][j] + nums_of_ways_ij[i][j-1]
                else:
                    nums_of_ways_ij[i][j] = 0  # If the current grid is an obstacle, set the number of ways as 0

        # Return the number of ways to reach the last grid
        return nums_of_ways_ij[-1][-1]