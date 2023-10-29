class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        positions = []
        if target in nums:
            first_index = nums.index(target)
            positions.append(first_index)
            first_index += 1
            while first_index < len(nums) and nums[first_index] == target:
                positions.append(first_index)
                first_index += 1
            return positions
        return []
        