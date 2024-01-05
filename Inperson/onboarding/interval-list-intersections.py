class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
   
        ptr1 = 0
        ptr2 = 0
        l1 = len(firstList)
        l2 = len(secondList)
        intersection = []

        while ptr1 < l1 and ptr2 < l2:
            if firstList[ptr1][1] > secondList[ptr2][1]:
                if firstList[ptr1][0] <= secondList[ptr2][1]:
                    pair = [max(firstList[ptr1][0], secondList[ptr2][0]), min(firstList[ptr1][1], secondList[ptr2][1])]
                    intersection.append(pair
                    )
                ptr2 += 1
            else:
                if firstList[ptr1][0] <= secondList[ptr2][1]:
                    pair = [max(firstList[ptr1][0], secondList[ptr2][0]), min(firstList[ptr1][1], secondList[ptr2][1])]
                    if pair[0] <= pair[1]:
                        intersection.append(pair)
                    
                ptr1 += 1
        return intersection