class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = col = len(image)
        for i in range(row):
            left = 0
            right = row-1
            while left < right:
                if image[i][left] == image[i][right]:
                    image[i][left] = image[i][right] = int(not image[i][right])
                left += 1
                right -= 1
            if row%2 !=0:
                image[i][row//2] = int(not image[i][row//2])
        return image

            