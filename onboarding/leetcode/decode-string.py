class Solution:
    def decodeString(self, s: str) -> str:
        def solve(current_idx):
            chars = []
            nums = []
            int_nums = 1
            i = current_idx
            while i < len(s) and s[i] != "]":
                if s[i].isdigit():
                    nums.append(s[i])
                elif s[i] == "[":
                    if nums:
                        int_nums = int(''.join(nums))
                    string, index = solve(i+1)
                    chars.append(int_nums * string)
                    i = index
                    nums = []
                    int_nums = 1
                else:
                    chars.append(s[i])
                i += 1
            return ''.join(chars), i
        
        return solve(0)[0]