class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # # 2, 1, 1, 2, 2

        # # 0 : 2, 1: 2, 2: 3, 3 :0, 4: 1

        # # #lets brute force
        # n = len(nums)
        # start_dest = {}
        # passes = {}
        # for i in range(n):
        #     start_dest[i] =( i + nums[i]) % n
        #     if i + nums[i] >= n or i + nums[i] < 0:
        #         passes[i] = True
        #     else:
        #         passes[i] = False
        
        # cycle = False
        # for i in range(n):
        #     one_loop = False
        #     steps = 0
        #     pass_ = False
        #     slow = start_dest[i]
        #     fast = start_dest[start_dest[i]]
        #     if slow == i:
        #         one_loop = True
        #     if slow == start_dest[slow]:
        #             one_loop = True
        #     while slow != fast and steps < n :
        #         if passes[slow] or passes[fast]:
        #             pass_ = True
        #         slow = start_dest[slow]
        #         if slow == start_dest[slow]:
        #             one_loop = True
        #         fast = start_dest[start_dest[fast]]
        #         steps += 1
        #     if slow == fast and not one_loop and slow == i and pass_:
        #         print(i)
        #         return True
        # return False

        n = len(nums)
        def dfs(curr_index, original_index, count, direction):
            if direction == 1 and nums[curr_index] < 0:
                return False
            if direction == -1 and nums[curr_index] > 0:
                return False
            if count  == 0:
                return False

            next_index = (curr_index + nums[curr_index]) % n
            if next_index == original_index:
                return True

            # if next_index == curr_index:
            #     return False 
            count -= 1
            return dfs(next_index, original_index, count, direction)

        soln = False
        for i in range(n):
            curr_index = (i + nums[i]) % n
            direction = nums[i] // abs(nums[i])
            if curr_index == i:
                continue
            if dfs(curr_index, i, n, direction):
                soln = True
        return soln
        

