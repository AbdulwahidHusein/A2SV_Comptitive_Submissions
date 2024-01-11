class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 0
        minop = 0
        minsofar = 10000

        while right < len(blocks):
            if blocks[right] == "W":
                minop += 1
            
            if right - left+1 >= k:
                minsofar = min(minsofar, minop)
                if blocks[left] == 'W':
                    minop -= 1
                left += 1
            right += 1
        return minsofar
        