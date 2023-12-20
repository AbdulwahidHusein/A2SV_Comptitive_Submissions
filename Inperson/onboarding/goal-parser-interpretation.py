class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        cmd = ""
        i = 0
        while i < n:
            if command[i] == "G":
                cmd += "G"
                i += 1
            elif command[i] == "(" and command[i+1] == ")":
                cmd += "o"
                i+=2
            else:
                cmd += "al"
                i+=4
        return cmd