class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_pascal = [1]
        for i in range(rowIndex):
            pascal = [1]
            for j in range(1, len(prev_pascal)):
                pascal.append(prev_pascal[j-1] + prev_pascal[j])
            pascal.append(1)

            prev_pascal = pascal.copy()
        return prev_pascal
